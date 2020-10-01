from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from courses.models import Course


class CourseListView(ListView):
    model = Course
    template_name = "courses/all_courses.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail_course.html"