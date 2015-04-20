from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# from django.shortcuts import HttpResponse
# from zuke.forms import DevicesForm
# Create your views here.

def index(request):
    return render(request, 'zuke/index.html', )


def about(request):
    return render(request, 'zuke/about.html', )


@login_required
def toggle(request):
    if request.POST.get('device_1'):
        print('user clicked device 1')
        return redirect(toggle)
    elif request.POST.get('device_2'):
        print('user clicked device 2')
        return redirect(toggle)
    elif request.POST.get('device_3'):
        print('user clicked device 3')
        return redirect(toggle)
    elif request.POST.get('device_4'):
        print('user clicked device 4')
        return redirect(toggle)
    else:
        return render(request, 'zuke/toggle.html', )