from django.urls import path

from courses.views import CourseListView, CourseDetailView

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='detail'),
]