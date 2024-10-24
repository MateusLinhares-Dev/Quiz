from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=150)
    code = models.CharField(verbose_name="Código", max_length=6, unique=True, null=False, blank=False, default="Código gerado após salvar a sala...")
    admin = models.ForeignKey(User, verbose_name="Administrador", on_delete=models.CASCADE, related_name="salas_criadas")
    create_date = models.DateTimeField(verbose_name="Data de criação",auto_now_add=True)

    def clean(self):
        """Validação dos forms"""
        if self.code:
            origem = Room.objects.filter(pk=self.pk).first()

            if origem:
                if origem.code != self.code:
                    raise ValidationError("O código da sala não pode ser alterado")
                if origem.name != self.name:
                    raise ValidationError("O nome da sala não pode ser alterado")
    
    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name
    