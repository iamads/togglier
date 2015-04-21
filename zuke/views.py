from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import zmq

xmpp_hostname = "ubuntu"

# from django.shortcuts import HttpResponse
# Create your views here.
context = zmq.Context()
# Define the socket using the "Context"
socket = context.socket(zmq.PAIR)

# Define the connection using socket command
socket.connect("tcp://127.0.0.1:5696")


def index(request):
    return render(request, 'zuke/index.html', )


def about(request):
    return render(request, 'zuke/about.html', )


@login_required
def toggle(request):
    username = request.user.username
    recepient = username + "@" + xmpp_hostname
    if request.POST.get('device_1_ON'):
        message = "device_1_ON"

    elif request.POST.get('device_1_OFF'):
        message = "device_1_OFF"

    elif request.POST.get('device_2_ON'):
        message = "device_2_ON"

    elif request.POST.get('device_2_OFF'):
        message = "device_2_OFF"

    elif request.POST.get('device_3_ON'):
        message = "device_3_ON"

    elif request.POST.get('device_3_OFF'):
        message = "device_3_OFF"

    elif request.POST.get('device_4_ON'):
        message = "device_4_OFF"

    elif request.POST.get('device_4_OFF'):
        message = "device_4_OFF"

    else:
        return render(request, 'zuke/toggle.html', )
    to_send = recepient + " " + message
    print to_send
    socket.send(to_send.encode('ascii'), copy=False)
    return redirect(toggle)