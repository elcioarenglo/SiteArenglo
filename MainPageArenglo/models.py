from django.db import models

class Cliente(models.Model):
    Nome = models.CharField(max_length=120)
    Email = models.EmailField()
    Mensagem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Nome