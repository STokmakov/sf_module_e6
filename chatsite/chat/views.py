from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import JSONParser

from chat.models import Message, Profile
from chat.forms import SignUpForm

from .serializers import ProfileSer, ProfileUpdateSer, RoomSer


from chat.models import Room


def index(request):
    if request.user.is_authenticated:
        return redirect('room-list')
    if request.method == 'GET':
        return render(request, 'chat/index.html', {})
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('room-list')


def register_view(request):
    """
    Render registration template
    """
    if request.method == 'POST':
        print("working1")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('room-list')
    else:
        print("working2")
        form = SignUpForm()
    template = 'chat/register.html'
    context = {'form':form}
    return render(request, template, context)

def profile(request):
    return render(request, 'chat/profile.html', {
        'profile': Profile.objects.all(),
    })

def profile_edit(request):
    return render(request, 'chat/profile_edit.html', {
        'profile': Profile.objects.all(),
    })

def room(request):
    return render(request, 'chat/room_list.html', {
        'rooms': Room.objects.all(),
    })

def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {
        'room': chat_room,
    })

def room_edit(request):
    return render(request, 'chat/room_edit.html', {
        'room': Room.objects.all(),
    })


class ProfileDetail(generics.RetrieveAPIView):
    """Профиль пользователя"""
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProfileUpdateView(generics.UpdateAPIView):
    """Редактирование профилья пользователя"""
    permission_classes = [permissions.AllowAny]  
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer

class RoomDetail(generics.RetrieveAPIView):
    """Комната"""
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSer

class RoomUpdateView(generics.UpdateAPIView):
    """Редактирование комнаты"""
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSer


