from django.shortcuts import render
from .models import Chart
import json
import time
from django.http import StreamingHttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def home(request):
    qs = Chart.objects.filter(number=2)
    context = {
        "qs": qs
    }
    return render(request, 'chart/home.html', context)


def event_stream():
    initial_data = ""
    while True:
        data = json.dumps(list(Chart.objects.filter(number=2).order_by("-id").values("number", "date")),
                          cls=DjangoJSONEncoder
                          )
        print(data)
        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data)
            initial_data = data
        time.sleep(1)


def stream(request):
    response = StreamingHttpResponse(event_stream())
    response['Content-Type'] = 'text/event-stream'
    return response
