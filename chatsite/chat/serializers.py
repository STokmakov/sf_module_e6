from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class UserSer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("username", "email")

class RoomSer(serializers.ModelSerializer):
    """Сериализация комнаты"""
    class Meta:
        model = Room
        fields = ("name",)

class ProfileSer(serializers.ModelSerializer):
    """Профиль пользователя"""
    user = UserSer()

    class Meta:
        model = Profile
        fields = ("user", "avatar", "email_two", "phone", "first_name", "last_name")


class ProfileUpdateSer(serializers.ModelSerializer):
    """Редактирование профиля пользователя"""
    class Meta:
        model = Profile
        fields = ("avatar", "email_two", "phone", "first_name", "last_name")
