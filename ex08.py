#Encapsulamento em Python - Aula 30-07
#Em python todos os métodos e classes em Python, são públicos.
#Alguns atributos e métodos só existem para funcionamento interno.
#Encapsulamento é uma técnica para ocultar detalhes internos.

#_ são do tipo protegido e não devem ser acessados pelo mudno externo, com ressalvas
#__(dois underlines) privado não devem ser acessados de forma nenhuma.

#getters e setters
#garantir que consigamos ocultar os dados.
#@property para verificar o comportamento do objeto

#PRÁTICA

class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome #dadoprotegido
        self.profissao = profissao #dadopúblico
        self.__identidade = identidade #dadoprotegido

    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self._identidade}'
        #Concatenamos

pessoa1 = Pessoa('Ana','Programadora','123456')
print(pessoa1)

#Ao tentar alterar um atributo público, o valor é alterado
pessoa1.profissao = 'Médica'
print(pessoa1)

#Ao tentar alterar um atributo privado, o valor não vai ser alterado.
pessoa1.__identidade = '2359595'
print(pessoa1)

#Conseguimos alterar um atributo protegido, se passarmos exatamente o caminho, vamos conseguir
pessoa1._nome = 'Marta'
print(pessoa1)

    