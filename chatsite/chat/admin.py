from django.contrib import admin
from chat.models import Message, Room, Profile

# Register your models here.
admin.site.register(Message)
admin.site.register(Room)




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ("user", "first_name", "last_name", "phone", "email_two")
    search_fields = ("user", "first_name", "last_name", "phone", "email_two")