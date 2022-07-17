from distutils.command.upload import upload
from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helper import *

# Create your models here.
class BlogUsers(models.Model): 
    id = models.AutoField(primary_key=True)       
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=40, default='NULL')
    birthdate = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True)

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.CharField(max_length=50)
    # image = models.ImageField(upload_to = "blog")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)


