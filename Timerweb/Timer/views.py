from django.shortcuts import render, redirect
from .forms import TimerForm
from .models import Timer
from django.http import HttpResponse
from datetime import datetime
from .forms import TimerForm


import csv

def homepage(request):
    return render(request,'Timer/homepage.html')



def start_timer(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    userName = request.user.username
    request.session[userName+'start_time'] = datetime.now().timestamp()

    return render(request, 'Timer/start_time.html', {'timer': timer})

def new_timer(request):
    userName = request.user.username
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session[userName+'name'] = name
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
    userName = request.user.username
    start_time = request.session.get(userName+'start_time')
    name = request.session.get(userName+'name')
    
    if start_time is None:
        # Handle the case when the timer hasn't started
        return HttpResponse("Timer hasn't started!")

    # Calculate the elapsed time
    current_time = datetime.now().timestamp()
    elapsed_time_seconds = int(current_time - start_time)

    if userName+'start_time' in request.session:
        del request.session[userName+'start_time']

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds-1,60))
    context = {
        'elapsed_time': format_time,
        'name':name
    }

    username = request.user.username
    data = [username,name,format_time]
    file_path = 'D:/Codes/Projects/Timer_Website/Timerweb/Timer/Data_time/timer_data.csv'

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName+'name' in request.session:
        del request.session[userName+'name']

    return render(request, 'Timer/elapsed_time.html', context)


def display_people(request):

    csv_file_path = 'D:/Codes/Projects/Timer_Website/Timerweb/Timer/Data_time/timer_data.csv'
    data_list = []

    user = request.user.username

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0]==user:
                data_list.append(row)
            else:
                pass
        
    if data_list==[]:
        error = {'error':"There are no records"}
        return render(request, 'Timer/display.html', error)
    else:
        context = {'data_list': data_list}
        return render(request, 'Timer/display.html', context)

def clear(request):
    csv_file_path = 'D:/Codes/Projects/Timer_Website/Timerweb/Timer/Data_time/timer_data.csv'
    user = request.user.username
    # Read existing data from the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader if row[0] != user]

    # Write the updated data (without the specified username) back to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

    return redirect('home')

if __name__ == '__main__':
    display_people("hello")