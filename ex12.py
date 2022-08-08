#Getter and Setter

class Pessoa(object):
    def __init__(self, nome, idade, salario):
        self._nome = nome #protegido
        self._idade = idade #protegido
        self._salario = salario #protegido

    @property
    def nome(self):
        print('get do nome')
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('set do nome', nome)
        self._nome = nome

    @property
    def idade(self):
        print('get da idade')
        return self._idade

    @idade.setter
    def idade(self, idade):
        print('set da idade', idade)
        self._idade = idade

    @property
    def salario(self):
        print('get do salario')
        return self._salario

    @salario.setter
    def salario(self, salario):
        print('set do salario', salario)
        self._salario = salario


pessoa = Pessoa('Miguel', 30, 50)
print(pessoa.__dict__) # valores iniciais
pessoa.nome = 'Afonso' #modifica nome 
pessoa.idade = 20 #modifica idade
pessoa.salario = 500 #modifica salário
print(pessoa.nome) #mostra a modificação de nome
print(pessoa.idade) #mostra a modificação de idade
print(pessoa.salario) #mostra a modificação de salário