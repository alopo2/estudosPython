#Definição da classe

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        if self.canal < self.canal_max:
            self.canal += 1 #incrementa
        
    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        if self.canal > self.canal_min:
            self.canal -= 1 #decrementa

    def aumentar_volume(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 10 #incrementa de 10 em 10

    def reduzir_volume(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume -= 10 #decrementa de 10 em 10

    def __str__(self) -> str: #informa que iremos trabalhar com uma string
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}' #formata para string, utilizamos a template string

#Criando instancias da class Televisao

tv_sala = Televisao()
tv_quarto = Televisao()

#Quando chamamos o método ligar() em uma instancia, estamos
#alterando apenas o estado dela. A outra televisao permanece desligada.
tv_sala.ligar() #Liga a tv da sala
tv_quarto.ligar() #Liga a tv do quarto
print('tv_sala está ligada? {}'.format(tv_sala.ligada)) #Vai retornar true, pq passamos a informação para ligá-la
print('tv_quarto está ligada {}'.format(tv_quarto.ligada)) #Vai retornar false, pq ainda não passamos nenhuma instrução para ligá-la

for _ in range(3):
    tv_sala.aumentar_volume()
print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))

#Imprimir o conteúdo do objeto
print('tv_sala:',tv_sala)
print('tv_quarto:',tv_quarto)

