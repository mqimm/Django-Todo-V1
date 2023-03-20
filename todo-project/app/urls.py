"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from todo.views import index_view, detail_view, create_view, update_view, delete_view

app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    path('<int:task_id>', detail_view, name='detail'),
    path('create', create_view, name='create'),
    path('update/<int:task_id>', update_view, name='update'),
    path('delete/<int:task_id>', delete_view, name='delete')
]
