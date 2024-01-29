from typing import Any
import random

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
    
    def attack(self,target):
        damage = self.__level * random.randint(1,3)
        target.receive_attack(damage)
        print(f"\n{self.get_name()} atacou {target.get_name()} e causou {damage} de dano")

    def special_attack(self,target):
        damage = self.__level * random.randint(5,7)
        target.receive_attack(damage)
        print(f"\n{self.get_name()} atacou {target.get_name()} com um ataque espcial e causou {damage} de dano")

    def receive_attack(self,damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0


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
    
