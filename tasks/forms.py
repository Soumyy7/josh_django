from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Task

# allows creation of users & tasks
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "mobile", "password1", "password2"]
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "status", "completed_at", "assigned_users"]
        widgets = {
            "completed_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
            "assigned_users": forms.SelectMultiple()
        }