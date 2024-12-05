from django.shortcuts import render, redirect
from .models import Debtor
from django.utils.timezone import now

def index(request):
    debtors = Debtor.objects.all()
    return render(request, 'index.html', {'debtors': debtors})

def add_debtor(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        amount = request.POST['amount']
        due_date = request.POST['due_date']
        Debtor.objects.create(name=name, phone=phone, amount=amount, due_date=due_date)
        return redirect('/')
    return render(request, 'add_debtor.html')


# views.py
from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('todo_list')

    return render(request, 'todo_list.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect('todo_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo_list')


from .models import Plan 

def plan_index(request):
    plans = Plan.objects.all()  # Barcha rejalarni olish
    return render(request, 'plan_index.html', {'plans': plans})

def delete_task2(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('plan_index')

from django.shortcuts import render, redirect
from .models import Plan

def welcome(request):
    """Render the welcome page."""
    return render(request, 'welcome.html')  # Replace with your welcome template path

def add_plan(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']  # Agar bu maydon kerak bo'lsa
        plan_type = request.POST['period']  # Periodni plan_type ga o'zgartirish

        # Plan obyektini yaratish
        Plan.objects.create(title=title, description=description, due_date=due_date, plan_type=plan_type)
        return redirect('/plan')  # Rejalar ro'yxati sahifasiga qaytish
    return render(request, 'add_plan.html')


# views.py
from django.shortcuts import render, redirect
from .models import Debtor, Plan

def index(request):
    debtors = Debtor.objects.all()
    return render(request, 'index.html', {'debtors': debtors})

def add_debtor(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        amount = request.POST['amount']
        due_date = request.POST['due_date']
        Debtor.objects.create(name=name, phone=phone, amount=amount, due_date=due_date)
        return redirect('index')
    
def delete_task1(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
    return render(request, 'add_debtor.html')

