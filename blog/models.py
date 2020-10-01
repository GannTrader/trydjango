from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class PostModel(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    body = models.TextField()
    likes = models.ManyToManyField(User)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)


STATUS = (
    ('active', 'active'),
    ('inactive', 'inactive'),
)

class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.CharField(max_length=25, blank=True, null=True)
    text = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS, default="inactive")
    created_at = models.DateTimeField(auto_now_add=True)

