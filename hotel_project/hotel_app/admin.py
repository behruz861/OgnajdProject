from django.contrib import admin
from .models import Room, BookApplication

class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('description',)}

admin.site.register(Room)
admin.site.register(BookApplication)