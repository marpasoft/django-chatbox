from django.conf import settings


def hookbox(request):
    return {
        'HOOKBOX_HOST': settings.HOOKBOX_HOST,
        'HOOKBOX_PORT': settings.HOOKBOX_PORT,
    }
