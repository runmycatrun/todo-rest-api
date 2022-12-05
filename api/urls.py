from django.urls import path
from .views import *


urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('task-list/', task_list, name='task-list'),
    path('task-detail/<int:pk>/', task_detail, name='task-detail'),
    path('task-create/', task_create, name='task-create'),
    path('task-update/<int:pk>/', task_update, name='task-update'),
    path('task-delete/<int:pk>/', task_delete, name='task-delete'),
]
