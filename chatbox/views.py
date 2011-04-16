from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson as json


@csrf_exempt
def connect(request):
    action = request.POST['action']
    conn_id = request.POST['conn_id']
    result = [True, {'name': "andrew"}]
    return HttpResponse(json.dumps(result), mimetype="application/json")


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
    return HttpResponse(json.dumps(result), mimetype="application/json")


@csrf_exempt
def subscribe(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    user = request.POST['user']

    options = {}
    result = [True, options]
    return HttpResponse(json.dumps(result), mimetype="application/json")


@csrf_exempt
def publish(request):
    action = request.POST['action']
    channel_name = request.POST['channel_name']
    payload = request.POST['payload']

    options = {}
    result = [True, options]
    return HttpResponse(json.dumps(result), mimetype="application/json")
