from django.urls import path

from courses.views import CourseListView, CourseDetailView, LessonView

urlpatterns = [
    path('', CourseListView.as_view(), name='course'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='detail'),
    path('lesson/<int:pk>', LessonView.as_view(), name='lesson'),
]