from django.db import models
#Import app models room, player
from room.models import Room
from player.models import Player

class Question(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="question")
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text
    
class Response(models.Model):

    MIN_RESPONSE = 2
    MAX_RESPONSE = 4
    question = models.ForeignKey(Question, on_delete=models.CASCADE, 
                                 related_name="questions"
                                 )
    correct = models.BooleanField(verbose_name="Está resposta é a correta?",
                                  default=False,
                                  null=False
                                  )
    text = models.TextField(verbose_name="Texto da resposta")

    def __str__(self) -> str:
        return self.text

class Scoring(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name="attempts")
    correct = models.BooleanField(verbose_name="Está pergunta é a correta?", default=False, null=False)
    points = models.IntegerField(verbose_name="Pontuação obtida", default=0)

    def __str__(self) -> str:
        return str(self.user)