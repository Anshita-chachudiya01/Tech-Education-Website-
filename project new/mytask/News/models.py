from django.db import models
from tinymce.models import HTMLField 
from autoslug import AutoSlugField

class news(models.Model): 
    news_title=models.CharField(max_length=100)
    content =  HTMLField() 




# Create your models here.
