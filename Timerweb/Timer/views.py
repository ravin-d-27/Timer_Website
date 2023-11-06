from django.shortcuts import render, redirect
from .forms import TimerForm
from .models import Timer

# Create your views here.

def homepage(request):
    return render(request,'Timer/homepage.html')

from .forms import TimerForm

def start_timer(request, timer_id):
    timer = Timer.objects.get(pk=timer_id)
    return render(request, 'Timer/start_time.html', {'timer': timer})

def new_timer(request):
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            timer = form.save()
            return redirect('start_timer', timer_id=timer.id)
    else:
        form = TimerForm()
    return render(request, 'Timer/new_timer.html', {'form': form})
