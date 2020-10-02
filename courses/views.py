from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from courses.models import Course, Lesson


class CourseListView(ListView):
    model = Course
    template_name = "courses/all_courses.html"


class CustomAccessMixin(AccessMixin):
    # login_url = 'verified_user' // or use below function is ok

    def get_login_url(self):
        return "verified_user"


class CourseDetailView(UserPassesTestMixin, CustomAccessMixin, DetailView):
    model = Course
    template_name = "courses/detail_course.html"
    raise_exception = False
    def test_func(self, **kwargs):
        _pk = self.kwargs["pk"]
        _course = Course.objects.get(pk=_pk)
        return self.request.user.groups.filter(name=_course.name)


class LessonView(UserPassesTestMixin, DetailView):
    model = Lesson
    template_name = "courses/lesson.html"

    def test_func(self, **kwargs):
        _pk = self.kwargs["pk"]
        _lesson = Lesson.objects.get(pk=_pk)
        return self.request.user.groups.filter(name=_lesson.course.name)