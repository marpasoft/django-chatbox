from django.contrib import admin

from chatbox.models import ChatMessage


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = [
        'message',
        'channel',
        'user',
        'created',
    ]
    raw_id_fields = [
        'user',
    ]

admin.site.register(ChatMessage, ChatMessageAdmin)
