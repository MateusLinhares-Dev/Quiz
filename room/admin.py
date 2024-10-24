from django.contrib import admin
from questionandanswer.models import Question, Response
from django.forms import ModelForm
from django.http import HttpRequest
from .models import Room
from typing import Any

# Configuração do admin para Room
class RoomAdmin(admin.ModelAdmin):
    model = Room
    search_fields = ['name', 'code']
    list_display = ["name", "code", "admin"]
    readonly_fields = ['code', 'admin']

    def save_model(self, request: HttpRequest, obj: Any, form: ModelForm, change: bool):
        if not obj.pk:
            obj.admin = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request: HttpRequest):
        """Filtrando por usuário"""
        qs = super().get_queryset(request)
    
        return qs.filter(admin=request.user)

admin.site.register(Room, RoomAdmin)