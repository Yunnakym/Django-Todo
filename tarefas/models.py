from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# criação do banco de dados
class Tarefas(models.Model):
    STATUS = (
        ("andamento", "Andamento"), 
        ("realizado", "Realizado"),
    )

    titulo = models.CharField(max_length=255)
    descrição = models.TextField()
    status = models.CharField(
        max_length=9,
        choices= STATUS,
    )

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)# data e hora de quando foi criado o elemento
    update_at = models.DateTimeField(auto_now=True) # quando a inf for atualizado

    def __str__(self):
        return self.titulo
