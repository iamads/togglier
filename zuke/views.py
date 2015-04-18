from django.shortcuts import render
from django.shortcuts import HttpResponse
from zuke.forms import DevicesForm
# Create your views here.


def index(request):
    context_dict = {'boldmessage': "I am from context"}
    return render(request, 'zuke/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "I m from about"}
    return render(request, 'zuke/about.html', context_dict)


def toggle(request):
    if request.method == 'POST':
        form = DevicesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = DevicesForm()
    return render(request, 'zuke/toggle.html', {'form': form})
