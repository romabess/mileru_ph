from django.contrib import admin
from .models import *



# Register your models here.

class User_baseAdmin(admin.ModelAdmin):
    list_display = ('user_login', 'user_pass', 'user_ip', 'user_device')
    search_fields = ('user_login', 'user_pass', 'user_ip')


class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('visitor_ip', 'visitor_country', 'vistor_agent', 'visit_time')
    search_fields = ('visitor_ip', 'visitor_country', 'vistor_agent', 'visit_time')

admin.site.register(User_base, User_baseAdmin)
admin.site.register(Visitors, VisitorsAdmin)
