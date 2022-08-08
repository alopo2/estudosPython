#O método Getter, retorna o valor;
#O método Setter, define ou atualiza;
#Costumam ser usados para cada instância.

class Quadrado:
    def __init__(self, medida):
        self.__altura = medida
        self.__largura = medida
    @property
    def altura(self):
        print('Getter de altura')
        return self.__altura
    @altura.setter
    def altura(self, valor):
        print('Setter de altura')
        if valor < 0:
            raise ValueError
        self.__altura = valor
    @property
    def largura(self):
        print('Getter da altura')
        return self.__largura
    @largura.setter
    def largura(self, valor):
        print('Setter de largura')
        if valor < 0:
            raise ValueError
        self.largura = valor
    def area(self):
        return self.largura * self.altura

quadrado1 = Quadrado(3)
print(quadrado1.altura)
print(quadrado1.largura)
print(quadrado1.area())
    