#Classes e objetos:

# Classe pessoa
# def fora de uma classe é função
# def dentro de uma classe é método
# self é o this do python
class Pessoa: 
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos')
        return

#Objeto pessoa1
pessoa1 = Pessoa('João', 20)
mensagem = pessoa1.saudacao()

#-------------------------------------------------------------#
# Herança e Polimorfismo

class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome

    def andar(self):
        print(f'O animal {self.nome} está andando')
        return

    def emitir_som(self):
        pass

# A classe animal herda os atributos e métodos da classe Cachorro
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
# O polimorfismo está intimamemnte ligado com a herança
# A classe gato herda o metodo emitir_som do animal
# Mas o subscreve e altera o seu funcionamento
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
dog = Cachorro(nome='Rex')
cat = Gato(nome='Napoleão')

print("\n Exemplo de polimorfimso")
animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} emite o som: {animal.emitir_som()}")

#-------------------------------------------------------------#
# Encapsulamento
# Permite que certas informações sejam protegidas 
class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo # Atributo privado

    # Os métodos protegem o antributo com verificações
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        
    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consulta_saldo(self,valor):
        return self.__saldo
    
#-------------------------------------------------------------#
# Abstração
# Classes abastratas são os moldes para outras classes
    
from abc import ABC, abstractmethod

class Veiculo(ABC):

    # A classe derivada dessa classe abstrata DEVERÁ definir 
    # as classes abstratas
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass