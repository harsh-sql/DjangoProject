from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('task1/', views.task_view, name='task_view'),
]
