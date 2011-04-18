from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name="index.html")), name="root_url"),
    url(r'^hookbox/', include('chatbox.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/', include('oauth_access.urls')),
    url(r'^linked_accounts/', include('linked_accounts.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
