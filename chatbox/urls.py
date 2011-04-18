from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('chatbox.views',
    url(r'^connect/$', 'connect', name='chatbox_connect'),
    url(r'^create_channel/$', 'create_channel', name='chatbox_create_channel'),
    url(r'^subscribe/$', 'subscribe', name='chatbox_subscribe'),
    url(r'^publish/$', 'publish', name='chatbox_publish'),
    url(r'^unsubscribe/$', 'unsubscribe', name='chatbox_unsubscribe'),
    url(r'^destroy_channel/$', 'destroy_channel', name='chatbox_destroy_channel'),
    url(r'^disconnect/$', 'disconnect', name='chatbox_disconnect'),
)
