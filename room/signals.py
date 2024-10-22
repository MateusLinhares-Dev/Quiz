from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Room

# Libs para gerar chave aleatória
import random
import string

@receiver(pre_save, sender=Room)
def room_pre_save(sender, instance, **kwargs):
    print("PRE SAVE")
    """Ao salvar gere uma chave aleatório para sala criada"""
    key = ''.join(random.choice(string.ascii_letters) for _ in range(6))

    #Adicionar o código gerado no campo code
    instance.code = key







