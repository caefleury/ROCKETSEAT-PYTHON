# Personagem: classe base
# Heroi: controlado pelo usuário
# Adversário: controlado pelo usúario

from typing import Any


class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"


class Hero(Character):
    def __init__(self, name, life, level, special_attack) -> None:
        super().__init__(name, life, level)
        self.__special_attack = special_attack

    def get_special_attack(self):
        return self.__special_attack

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_special_attack()}"


class Enemy(Character):
    def __init__(self, name, life, level, type) -> None:
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}\nTipo: {self.get_type()}"


# heroi = Hero(name='Sergio Sacani', life=100,
#              level=164, special_attack="Foguetes")
# print(heroi.show_details())

# enemy = Enemy(name='Terraplanista genérico', life=60, level=230, type='Burro')
# print(enemy.show_details())

class Game:
    def __init__(self) -> None:
        self.hero = Hero(name='Sergio Sacani', life=100, level=164, special_attack="Foguetes")
        self.enemy = Enemy(name='Terraplanista genérico', life=60, level=230, type='Burro')

    def start_battle(self):
        """ Gestão de batalhas em turnos """
        print("Iniciando batalha")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("Detalhes dos personagens")
            print("Detalhes do heroi")
            print(self.hero.show_details())
            print("Detalhes do inimigo ")
            print(self.enemy.show_details())

            input("Pressione Enter para atacar....")
            escolha = input("Escolha (1 -  Ataque Normal, 2 - Ataque especial): ")

#Criar instância do jogo e inciar batalha
jogo = Game()
jogo.start_battle()