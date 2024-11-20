from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.task_create_view, name='task_create'),
    path('list/', views.task_list_view, name='task_list'),
    path('update/<int:id>/', views.task_update_view, name='task_update'),
    path('delete/<int:id>/', views.task_delete_view, name='task_delete'),
]