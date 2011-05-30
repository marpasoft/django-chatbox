import logging
import iso8601

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson as json

from chatbox.models import ChatMessage


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
        "history_size": 0,
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

    data = json.loads(payload)
    user = request.user

    ChatMessage.objects.create(
        channel=channel_name,
        message=data['message'],
        user=user,
        created=iso8601.parse_date(data['date']).replace(tzinfo=None))

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
