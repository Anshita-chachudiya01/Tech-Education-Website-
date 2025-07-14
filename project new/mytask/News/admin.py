from django.contrib import admin
from News.models import news

class newadmin(admin.ModelAdmin):
    list_display=('news_title' , 'content')

admin.site.register(news,newadmin)


# Register your models here.
