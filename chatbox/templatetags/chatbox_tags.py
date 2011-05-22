from django import template
from django.conf import settings
from django.utils import simplejson as json

from chatbox.models import ChatMessage


register = template.Library()

@register.simple_tag
def chat_history(channel, limit=20):
    messages = ChatMessage.objects.filter(
        channel=channel).order_by('-created').select_related('user')[0:limit]
    def make_frame(msg):
        return {
            'payload': {
                'message': msg.message,
                'date': msg.created.strftime('%Y-%m-%dT%H:%M:%SZ'),
            },
            'user': msg.user.username,
        }

    messages = list(messages)
    messages.reverse()

    history = map(lambda x: ('PUBLISH', make_frame(x)), messages)
    return json.dumps(history)
