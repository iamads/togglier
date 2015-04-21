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
    if request.POST.get('device_1'):
        message = "device_1 ON"

    elif request.POST.get('device_2'):
        message = "device_1 OFF"

    elif request.POST.get('device_3'):
        message = "device_3"

    elif request.POST.get('device_4'):
        print('user clicked device 4')
        message = "device_4"

    else:
        return render(request, 'zuke/toggle.html', )
    socket.send(recepient+" "+message)
    return redirect(toggle)