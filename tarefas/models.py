from django.db import models

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

    created_at = models.DateTimeField(auto_now_add=True)# data e hora de quando foi criado o elemento
    update_at = models.DateTimeField(auto_now=True) # quando a inf for atualizado

    def __str__(self):
        return self.titulo
