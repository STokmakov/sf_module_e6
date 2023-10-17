from django.contrib.auth import logout
from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.room, name='room-list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('chat/<str:room_name>/', views.room_view, name='chat-room'),
    path('profile/', views.profile, name='prof-user'),
    path('profile/update/', views.profile_edit, name='prof-user_edit'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('update/<int:pk>/', views.ProfileUpdateView.as_view()),
    path("room/", views.room_edit, name='room-edit'),
    path('room/<int:pk>/', views.RoomDetail.as_view()),
    path('room/update/<int:pk>/', views.RoomUpdateView.as_view()),

]
