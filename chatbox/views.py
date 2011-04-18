import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson as json


def render_json(obj):
    return HttpResponse(json.dumps(obj), mimetype="application/json")


logger = logging.getLogger(__name__)


@csrf_exempt
def connect(request):
    logging.info(request.POST)
    if request.user.is_authenticated():
        result = [True, {'name': request.user.username}]
    else:
        result = [False, {}]
    return render_json(result)


@csrf_exempt
def create_channel(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    options = {
        "history_size": 20,
        "reflective": True,
        "presenceful": True,
    }
    result = [True, options]
    return render_json(result)


@csrf_exempt
def subscribe(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    user = request.POST['user']

    options = {}
    result = [True, options]
    return render_json(result)


@csrf_exempt
def publish(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    payload = request.POST['payload']

    options = {}
    result = [True, options]
    return render_json(result)


@csrf_exempt
def unsubscribe(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    user = request.POST['user']

    options = {}
    result = [True, options]
    return render_json(result)


@csrf_exempt
def destroy_channel(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    options = {}
    result = [True, options]
    return render_json(result)


@csrf_exempt
def disconnect(request):
    action = request.POST['action']
    result = [True, {}]
    return render_json(result)
