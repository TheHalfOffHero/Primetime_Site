from django.db import models

# Create your models here.
class post(models.Model):
    #Fields of the model posts, I think I need a date, title, and
    #a field for the body of the text at minimum. Subject to Change.
    title = models.CharField(max_length=200)
    body = models.TextField()
    