from django.urls import path
from . import views
from .views import todo_list, toggle_task, delete_task, delete_task1, delete_task2


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('plan/', views.plan_index, name='plan_index'),
    path('add1/', views.add_plan, name='add_plan'),
    path('index/', views.index, name='index'),
    path('add/', views.add_debtor, name='add_debtor'),
    path('todo/', todo_list, name='todo_list'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('delete1/<int:task_id>/', delete_task, name='delete_task1'),
    path('delete2/<int:task_id>/', delete_task, name='delete_task2'),    
]

# need to be refactored and reanalyzed
