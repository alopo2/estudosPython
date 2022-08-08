#Classes descrevem o que um objeto vai ser, mas elas não criam o objeto em si

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False
tv_sala = Televisao()
tv_sala.ligar()
tv_sala

#O método é associado a uma classe, e uma classe é associada a um objeto
#O self representa a instancia da nossa classe
#self.canal/self.ligada representa o objeto em si
