#Exemplo Estacionamento

class Carro:
    def __init__(self, cor, modelo,id_placa):
        self.cor = cor
        self.ligado = False
        self.modelo = modelo
        self.velocidade = 0
        self.placa = id_placa
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if self.ligado == True:
            self.velocidade += 2 #incrementa

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > 0:
            self.velocidade -= 10 #decrementa

    def __str__(self) -> str: #informa que iremos trabalhar com uma string
        return f'Carro - ligado {self.ligado} - cor {self.cor} - modelo{self.modelo} - velocidade_atual - {self.velocidade}'
class Moto():
    def __init__(self, cor, modelo,id_placa):
        self.cor = cor
        self.ligado = False
        self.modelo = modelo
        self.velocidade = 0
        self.placa = id_placa
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if self.ligado == True:
            self.velocidade += 2 #incrementa

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > 0:
            self.velocidade -= 10 #decrementa
class Vaga():
    def __init__(self, id, tipo, placa,livre):
        self.id = id
        self.tipo = tipo
        self.placa = placa
        self.livre = True
    def ocupar():
        self.livre = True
    def desocupar():
        self.livre = False

#carro1 = Carro('Preto','HondaCity')
#print(carro1)

#carro1.ligar() #Liga o carro
#for i in range(4):
#    carro1.acelerar()
#print(carro1)

#carro1.desligar() #Desliga o carro
#for i in range(8):
#    carro1.desacelerar()
#print(carro1)
    