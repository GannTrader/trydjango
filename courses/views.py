from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from courses.models import Course, Lesson


class CourseListView(ListView):
    model = Course
    template_name = "courses/all_courses.html"


class CourseDetailView(UserPassesTestMixin, DetailView):
    model = Course
    template_name = "courses/detail_course.html"

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