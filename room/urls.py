from django.urls import path
from .views import index, room_detail

urlpatterns = [
    path('', index, name="inicio"),
    path('sala/<str:code>/jogador/<str:id_player>', room_detail, name='room_detail')
]