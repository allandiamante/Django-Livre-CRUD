from django.db import models

# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    #Exibirá uma descrição, quando o objeto for chamado
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    #Exibirá uma descrição, quando o objeto for chamado
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=150)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)


class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.DecimalField(decimal_places=1, max_digits=4)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    
    def __str__(self):
        return "{} - {} ({})".format(self.nome, self.descricao, self.nivel)

class Campus(models.Model):
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    telefone = models.DecimalField(decimal_places=0, max_digits=9)
    
    def __str__(self):
        return "{} - {} ({})".format(self.cidade, self.endereco, self.telefone)
