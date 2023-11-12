from django.shortcuts import render, redirect
from .forms import TimerForm
from .models import Timer

import csv
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.

def homepage(request):
    return render(request,'Timer/homepage.html')

from .forms import TimerForm

def start_timer(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    request.session['start_time'] = datetime.now().timestamp()

    return render(request, 'Timer/start_time.html', {'timer': timer})

def new_timer(request):
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            timer = form.save()
            return redirect('start_timer', timer_id=timer.id)
    else:
        form = TimerForm()
    return render(request, 'Timer/new_timer.html', {'form': form})


def start_timer2(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    return render(request, 'Timer/start_time2.html', {'timer': timer})

def new_timer2(request):
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            timer = form.save()
            return redirect('start_timer2', timer_id=timer.id)
    else:
        form = TimerForm()
    return render(request, 'Timer/new_timer2.html', {'form': form})

def elapsed_time(request):
    # Retrieve the start time from the session
    start_time = request.session.get('start_time')
    name = request.session.get('name')
    
    if start_time is None:
        # Handle the case when the timer hasn't started
        return HttpResponse("Timer hasn't started!")

    # Calculate the elapsed time
    current_time = datetime.now().timestamp()
    elapsed_time_seconds = int(current_time - start_time)

    if 'start_time' in request.session:
        del request.session['start_time']

    context = {
        'elapsed_time': elapsed_time_seconds-1,
    }

    username = request.user.username
    data = [username,name,elapsed_time_seconds-1]
    file_path = 'D:/Codes/Projects/Timer_Website/Timerweb/Timer/Data_time/timer_data.csv'

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if 'name' in request.session:
        del request.session['name']

    return render(request, 'Timer/elapsed_time.html', context)