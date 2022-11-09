from django.db import models

class Registro(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.IntegerField()

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.nome, self.telefone)
