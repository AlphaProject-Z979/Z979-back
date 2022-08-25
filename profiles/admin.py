from atexit import register
from django.contrib import admin
from .models import User

class profileAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,profileAdmin)