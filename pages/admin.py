from django.contrib import admin

from .models import Notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receptor', 'title', 'datetime_created')