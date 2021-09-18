from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

STATUS = (
    (0,"Draft"),
    (1, "Publish")
)

# Create your models here.
class post(models.Model):
    #Fields of the model posts
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='Forum_Post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title