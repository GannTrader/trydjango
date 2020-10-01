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