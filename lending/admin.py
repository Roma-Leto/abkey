from django.contrib import admin
from .models import ABKUsersModel, MessageClient


admin.site.register(ABKUsersModel)


class MsgAdmin(admin.ModelAdmin):
    list_display = (
        'name_user',
        'email_user',
        'subject_message',
        'message',
        'time_send',
    )


admin.site.register(MessageClient, MsgAdmin)
