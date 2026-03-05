from django.shortcuts import render
from StudApp.models import Students, Contacts
from StudApp.serializers import StudentSerializer, ContactSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    model = Students

class StudentCourseFilter(APIView):
    def get(self, request, c_name):
        students = Students.objects.filter(course=c_name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StudentAgeFilter(APIView):
    def get(self,request, age):
        students = Students.objects.filter(age__gt=age)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StudentNameFilter(APIView):
    def get(self, request, name_contain):
        students = Students.objects.filter(name__icontains=name_contain)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentCount(APIView):
    def get(self, request):
        courses = Students.objects.values_list('course', flat=True)
        course_count = {}
        result = {}

        for course in courses:
            if course in course_count:
                course_count[course] += 1
            else:
                course_count[course] = 1

        for course, count in course_count.items():
            result[course] = f"{count} students"
        
        return Response(result)
    
class ContactView(APIView):
    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactCheckView(APIView):
    def post(self, request):
        mobile_number = request.data.get('mobile')

        if not mobile_number:
            return Response({"message":"Mobile number is required"}, status=status.HTTP_400_BAD_REQUEST)

        if Contacts.objects.filter(mobile=mobile_number).exists():
            return Response({"message":"Mobile number already registered"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Mobile number not found"}, status=status.HTTP_404_NOT_FOUND)


