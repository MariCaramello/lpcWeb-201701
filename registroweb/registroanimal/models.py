from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=200)  # atributo público
    locomocao = models.CharField(max_length=50)  # atributo público
    respiracao = models.CharField(max_length=50)  # atributo público
    tiporeproducao = models.ForeignKey('TipoReproducao')  # atributo público
    tipohabitat = models.ForeignKey('TipoHabitat')  # atributo público


    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat):
        super(Animal, self).__init__()
        self.nome = nome
        self.locomocao = locomocao
        self.respiracao = respiracao
        self.tiporeproducao = tiporeproducao
        self.tipohabitat = tipohabitat

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat)

    def vocal(self):
        vocalizacao = models.CharField(max_length=100)
        return vocalizacao

class Peixe(Animal):
    nomepeixe = models.CharField(max_length=200, default='nomepeixe')
    nadadeira = models.CharField(max_length=50)
    escama = models.CharField(max_length=10)

    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat, nomepeixe,  nadadeira, escama):
        Animal.__init__(nome, locomocao, respiracao, tiporeproducao, tipohabitat)
        self.__nomepeixe = nomepeixe
        self.__nadadeira = nadadeira
        self.__escama = escama

    def getNomepeixe(self, i):
        return self.__nomepeixe[i]

    def getNadadeira(self, i):
        return self.__nadadeira[i]

    def getEscama(self,i):
        return self.__escama[i]

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat, self.__nadadeira, self.__escama)

    def vocal(self):
        Animal.vocal(vocalizacao = models.CharField(max_length=100))

class Anfibio(Animal):
    nomeanfibio = models.CharField(max_length=200, default='nomeanfibio')
    cauda = models.CharField(max_length=10)

    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat, nomeanfibio, cauda):
        Animal.__init__(nome, locomocao, respiracao, tiporeproducao, tipohabitat)
        self.__nomeanfibio = nomeanfibio
        self.__cauda = cauda

    def getNomeanfibio(self, i):
        return self.__nomeanfibio[i]

    def getCauda(self, i):
        return self.__cauda[i]

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat, self.__cauda)

class Repteis(Animal):
    nomerepteis = models.CharField(max_length=200, default='nomerepteis')
    classe = models.CharField(max_length=50)

    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat, nomerepteis, classe):
        Animal.__init__(nome, locomocao, respiracao, tiporeproducao, tipohabitat)
        self.__nomerepteis = nomerepteis
        self.__classe = classe

    def getNomerepteis(self, i):
        return self.__nomerepteis[i]

    def getClasse(self, i):
        return self.__classe[i]

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat, self.__classe)

class Ave(Animal):
    nomeave = models.CharField(max_length=200, default='nomeave')
    voa = models.CharField(max_length=10)

    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat, nomeave, voa):
        Animal.__init__(nome, locomocao, respiracao, tiporeproducao, tipohabitat)
        self.__nomeave = nomeave
        self.__voa = voa

    def getNomeave(self, i):
        return self.__nomeave[i]

    def getVoa(self, i):
        return self.__voa[i]

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat, self.__voa)

class Mamifero(Animal):
    nomemamifero = models.CharField(max_length=200, default='nomemamifero')
    pelo = models.CharField(max_length=10)

    def __init__(self, nome, locomocao, respiracao, tiporeproducao, tipohabitat, nomemamifero, pelo):
        Animal.__init__(nome, locomocao, respiracao, tiporeproducao, tipohabitat)
        self.__nomemamifero = nomemamifero
        self.__pelo = pelo

    def getNomemamifero(self, i):
        return self.__nomemamifero[i]

    def getPelo(self, i):
        return self.__pelo[i]

    def __str__(self):
        return str(self.nome, self.locomocao, self.respiracao, self.tiporeproducao, self.tipohabitat, self.__pelo)

class TipoReproducao(models.Model):
    nomereproducao = models.CharField(max_length=50)
    detalhe = models.CharField(max_length=500)

class TipoHabitat(models.Model):
    nomehabitat = models.CharField(max_length=50)


