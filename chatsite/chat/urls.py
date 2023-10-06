from django.contrib.auth import logout
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.room, name='room-list'),
  #  path('<str:room_name>/', views.room_view, name='chat-room'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('chat/<str:room_name>/', views.room_view, name='chat-room'),
]
