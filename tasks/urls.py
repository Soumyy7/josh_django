from django.urls import path, re_path
from django.shortcuts import redirect
from .views import (
    all_tasks_view, user_tasks_view, assign_task_form_view, 
    create_task_form_view, task_detail_view
)

urlpatterns = [
    # home page, lists all the currently present tasks with their summarized details
    path('tasks/', all_tasks_view, name='all-tasks'),

    # fetches all tasks assigned to a specific user
    path('tasks/user/<str:username>/', user_tasks_view, name='user-tasks-view'),

    # Redirect /tasks/user/ (without a username) to /tasks/
    re_path(r'^tasks/user/$', lambda request: redirect('/tasks/', permanent=False)),

    # allows assigning a task to a user, can assign a task to multiple users at once
    path('tasks/assign/', assign_task_form_view, name='assign-task-form'),

    # helps in creating new tasks through form inputs
    path('tasks/create/', create_task_form_view, name='create-task-form'),

    # more for functionality, the route where each task and all their details are present, helps in re-routing user to adn from a task to the homepage
    path('tasks/<str:task_name>/', task_detail_view, name = 'task-detail'),

]
