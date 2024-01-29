# Personagem: classe base
# Heroi: controlado pelo usuário
# Adversário: controlado pelo usúario

from characters import Hero, Enemy


class Game:
    def __init__(self) -> None:
        self.hero = Hero(name='Sergio Sacani', life=100,
                         level=5, special_attack="Foguetes")
        self.enemy = Enemy(name='Terraplanista genérico',
                           life=80, level=3, type='Burro')

    def start_battle(self):
        """ Gestão de batalhas em turnos """
        print("Iniciando batalha")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos personagens")
            print("\nDetalhes do heroi")
            print(self.hero.show_details())
            print("\nDetalhes do inimigo ")
            print(self.enemy.show_details())

            input("Pressione Enter para atacar....")
            choice = input("Escolha (1 - Ataque Normal, 2 - Ataque especial):")

            if choice == '1':
                self.hero.attack(self.enemy)
            elif choice == '2':
                self.hero.special_attack(self.enemy)
            else:
                print("Escolha invalida, escolha novamente")

            if self.enemy.get_life() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print(f"Parabens {self.hero.get_name()}, você venceu a batalha!")
        else:
            print("Que pena, o inimigo venceu a batalha")


jogo = Game()
jogo.start_battle()
