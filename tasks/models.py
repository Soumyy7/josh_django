from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

# model to create new users, defines the requisites, like name(username), email, mobile
class CustomUser(AbstractUser):
    """Represents a user in the system."""
    name = models.CharField(max_length=255, null=True, blank=True)  # Optional name field
    email = models.EmailField(unique=True)  # Enforcing unique email
    mobile = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{10,15}$', message="Enter a valid mobile number")]
    )
    # defines the string printed on printing an object of this call
    def __str__(self):
        return self.username

# model to create tasks, with fields like name, description, type, completion time and assigned users
class Task(models.Model):
    """Represents a task in the system."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100, null=True, blank=True)  # Optional
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(CustomUser, related_name="tasks")  # Many users can be assigned

    # defines the string printed on printing an object of this call
    def __str__(self):
        return self.name