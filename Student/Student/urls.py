"""
URL configuration for Student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StudApp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentView, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course_filter/<c_name>', StudentCourseFilter.as_view(), name="course_filter"),
    path('age_filter/<int:age>', StudentAgeFilter.as_view(), name="age_filter"),
    path('name_filter/<name_contain>', StudentNameFilter.as_view(), name="name_filter"),
    path('student_count/', StudentCount.as_view(), name="student_count"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('contact_check/', ContactCheckView.as_view(), name="contact_check"),
] + router.urls
