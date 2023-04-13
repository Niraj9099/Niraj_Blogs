from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
# Create your models here.
class blog_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.TextField(max_length=100)
    disc = HTMLField()
    img = models.ImageField(upload_to='blogimg')


class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()