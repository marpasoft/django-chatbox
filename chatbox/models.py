from datetime import datetime

from django.db import models


class ChatMessage(models.Model):
    channel = models.CharField(max_length=255, db_index=True)
    message = models.TextField(default='')
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return  u'%s - %s' % (self.channel, self.message)
