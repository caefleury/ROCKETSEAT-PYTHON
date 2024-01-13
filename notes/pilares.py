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

# Abstração