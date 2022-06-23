from django.db import models

class Cliente(models.Model):


    def dataCadastro(self):
        Consultar_Imoveis = models.CharField(max_length=100)
        Manter_Conta = models.CharField(max_length=100)
        Agendar_visita = models.CharField(max_length=100)
        return self.dataCadastro
