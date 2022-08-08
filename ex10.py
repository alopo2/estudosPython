#Herança uma classe pode herdar os métodos e propriedades de outra classe
#Estudante herdando pessoa
#Permite modelar relações do mundo real
#Em Python, todas as classes herdam implicitamente da classe object, que fornece
#métodos comuns que podem ser sobrescritos como o __init__, o __str__ e outros.
#Exemplo: Professor > Trabalhador > Pessoa

class Pessoa: #criando objeto pessoa
    def __init__(self, nome):
        self._nome = nome #ambos protegidos
        self._tipo = 'Pessoa' #tipo string pessoa
    
    def falar_oi(self):
        print('Oi, meu nome é {}'.format(self._nome))
    
    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Maria')
pessoa.falar_oi()
pessoa.falar_tipo()

#A classe Estudante é derivada da classe Pessoa
#Relação: Estudante é uma pessoa
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome) #chama o construtor na classe base        
        self._curso = curso
    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso {self._curso}')
        #A propriedade self._nome é herdada da classe base
    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()
estudante = Estudante('Yasmin','Introdução a Linguagem Python')
estudante.falar_oi() #o método falar_oi é herdado da classe base
estudante.falar_tipo() #o método falar_tipo é herdado da clalsse base, e sobreescrito na classe derivada.
estudante.falar_curso() 