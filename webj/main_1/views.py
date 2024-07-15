# main_1/views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def new(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm()
    return render(request, 'main_1/new.html', {'form': form})

def index(request):
    messages = Message.objects.all()
    return render(request, 'main/index.html', {'messages': messages})


def data(request):
    return render(request, 'main_1/data.html')

def test(request):
    return render(request, 'main_1/test.html')