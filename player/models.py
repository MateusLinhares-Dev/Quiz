from django.db import models
from room.models import Room

class Player(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(verbose_name="Pontuação total", default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="player")
    date_input = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']