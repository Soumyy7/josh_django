from rest_framework import serializers
from .models import CustomUser, Task

#interprets django model instances into json for api calls
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'