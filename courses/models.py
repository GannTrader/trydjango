from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField()
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson} -- {self.course.name}"
