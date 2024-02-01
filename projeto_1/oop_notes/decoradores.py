from typing import Any

# Um decorador é um tipo especial de função que permite modificar ou
# estender o comportamento de outras funções,
# sem precisar alterar o código original delas.

# Decorador de função


def meu_decorador(func):
    def wrapper():
        print("Antes da minha função ser chamada")
        func()
        print("Depois da função ser chamada")

    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()

# Podem existir decoradores como classes


class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes de função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")
        pass


@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")


segunda_funcao()
