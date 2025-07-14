from django.contrib import admin
from service.models import Service

class serviceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title', 'Service_des')

admin.site.register(Service,serviceAdmin)

# Register your models here.





















