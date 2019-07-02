from django.db import models
from base.models import Pessoa

class Aluno(models.Model):
    ra = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.ra
