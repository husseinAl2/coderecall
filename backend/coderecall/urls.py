"""
URL configuration for coderecall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# To return JSON responses directly from URLs
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

def index(request):
    return JsonResponse({"app": "CodeRecall", "status": "running"})

urlpatterns = [
    path('admin/', admin.site.urls),

    # Simple health check endpoint
    path('health/', health),
    path("", index),
]
