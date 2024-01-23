from django.shortcuts import render, redirect
from .forms import TimerForm
from .models import Timer
from django.http import HttpResponse
from datetime import datetime
from .forms import TimerForm
import csv

# Change this path according to your Machine
file_path = '/home/RavinD27Toastmasters/Timer_Website/Timerweb/Timer/Data_time/timer_data.csv'



def homepage(request):

    userName = request.user.username

    # Closing the unwanted sessions
    if userName+'start_time' in request.session:
        del request.session[userName+'start_time']

    if userName+'name' in request.session:
        del request.session[userName+'name']

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
    userName = request.user.username
    request.session[userName+'start_time'] = datetime.now().timestamp()

    return render(request, 'Timer/start_time2.html', {'timer': timer})

def new_timer2(request):
    userName = request.user.username
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session[userName+'name'] = name
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

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds,60))
    context = {
        'elapsed_time': format_time,
        'name':name
    }

    username = request.user.username
    data = [username,name,format_time,"Table Topic Session"]
    

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName+'name' in request.session:
        del request.session[userName+'name']

    return render(request, 'Timer/elapsed_time.html', context)

def elapsed_time2(request):
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

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds,60))
    context = {
        'elapsed_time': format_time,
        'name':name
    }

    username = request.user.username
    data = [username,name,format_time,"Prepared Speech"]
    

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName+'name' in request.session:
        del request.session[userName+'name']

    return render(request, 'Timer/elapsed_time2.html', context)


def display_people(request):

    csv_file_path = file_path
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
        ty = ['Debate Session', 'Table Topic Session', 'Prepared Speech', "Educational Speech"]
        deb = [i for i in data_list if i[3] == ty[0]]
        table = [i for i in data_list if i[3] == ty[1]]
        prep = [i for i in data_list if i[3] == ty[2]]
        edu = [i for i in data_list if i[3] == ty[3]]

        all_names = [i[0] for i in data_list]

        context = {'data_list': data_list, 'deb': deb, 'table': table, 'prep': prep, 'edu': edu, 'all_names': all_names}
        return render(request, 'Timer/display.html', context)


def clear(request):
    csv_file_path = file_path
    user = request.user.username
    # Read existing data from the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader if row[0] != user]

    # Write the updated data (without the specified username) back to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

    message = {"message":"Your Data has been cleared successfully"}
    return render(request, "Timer/homepage.html", message)
    
    
    
# views.py

def new_timer3(request):
    userName = request.user.username

    if request.method == 'POST':
        form = TimerForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            is_captain = form.cleaned_data['is_captain']
            
            print(is_captain)

            request.session[userName + 'name'] = name

            timer = form.save()
            
            if is_captain == True:
                return redirect('start_timer3', timer_id=timer.id)
            else:
                return redirect('start_timer3a', timer_id=timer.id)
    else:
        form = TimerForm()

    return render(request, 'Timer/new_timer3.html', {'form': form})

def start_timer3(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    userName = request.user.username
    request.session[userName + 'start_time'] = datetime.now().timestamp()
    return render(request, 'Timer/start_time3.html', {'timer': timer})

def start_timer3a(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    userName = request.user.username
    request.session[userName + 'start_time'] = datetime.now().timestamp()
    return render(request, 'Timer/start_time3a.html', {'timer': timer})

def elapsed_time3(request):
    # Retrieve the start time and user details from the session
    userName = request.user.username
    start_time = request.session.get(userName + 'start_time')
    name = request.session.get(userName + 'name')

    if start_time is None:
        # Handle the case when the timer hasn't started
        return HttpResponse("Timer hasn't started!")

    # Calculate the elapsed time
    current_time = datetime.now().timestamp()
    elapsed_time_seconds = int(current_time - start_time)

    if userName + 'start_time' in request.session:
        del request.session[userName + 'start_time']

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds, 60))
    context = {
        'elapsed_time': format_time,
        'name': name,
    }

    username = request.user.username
    data = [username, name, format_time, "Debate Session"]

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName + 'name' in request.session:
        del request.session[userName + 'name']

    return render(request, 'Timer/elapsed_time3.html', context)


def elapsed_time3a(request):
    # Retrieve the start time and user details from the session
    userName = request.user.username
    start_time = request.session.get(userName + 'start_time')
    name = request.session.get(userName + 'name')

    if start_time is None:
        # Handle the case when the timer hasn't started
        return HttpResponse("Timer hasn't started!")

    # Calculate the elapsed time
    current_time = datetime.now().timestamp()
    elapsed_time_seconds = int(current_time - start_time)

    if userName + 'start_time' in request.session:
        del request.session[userName + 'start_time']

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds, 60))
    context = {
        'elapsed_time': format_time,
        'name': name,
    }

    username = request.user.username
    data = [username, name, format_time, "Debate Session"]

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName + 'name' in request.session:
        del request.session[userName + 'name']

    return render(request, 'Timer/elapsed_time3a.html', context)

def credits(request):
    return render(request, "Timer/credits.html")







def start_timer_edu(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    userName = request.user.username
    request.session[userName+'start_time'] = datetime.now().timestamp()

    return render(request, 'Timer/start_timer_edu.html', {'timer': timer})

def new_timer_edu(request):
    userName = request.user.username
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session[userName+'name'] = name
            timer = form.save()
            return redirect('start_time_edu', timer_id=timer.id)
    else:
        form = TimerForm()
    return render(request, 'Timer/new_timer_edu.html', {'form': form})
    
    
def elapsed_time_edu(request):
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

    format_time = "{} minutes and {} seconds".format(*divmod(elapsed_time_seconds,60))
    context = {
        'elapsed_time': format_time,
        'name':name
    }

    username = request.user.username
    data = [username,name,format_time,"Educational Speech"]
    

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data
        writer.writerow(data)

    if userName+'name' in request.session:
        del request.session[userName+'name']

    return render(request, 'Timer/elapsed_time_edu.html', context)




if __name__ == '__main__':
    display_people("hello")