from django.shortcuts import render, redirect
from .models import Habit

def home(request):
    habits = Habit.objects.all()
    return render(request, 'habitsApp/home.html', {'habits': habits})

def add_habit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')
        Habit.objects.create(name=name, description=desc)
        return redirect('home')
    return render(request, 'habitsApp/add_habit.html')

def toggle_habit(request, id):
    habit = Habit.objects.get(id=id)
    habit.is_completed_today = not habit.is_completed_today
    habit.save()
    return redirect('home')