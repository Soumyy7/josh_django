from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

urlpatterns = [
    path('admin', admin.site.urls),
    
    # responsible for displaying the app routes in this django project
    path('', include('tasks.urls')),

    # Catch-all routes other than a valid route and re-direct to the homepage
    re_path(r'^.*$', lambda request: redirect('/tasks/', permanent=False)),
]
