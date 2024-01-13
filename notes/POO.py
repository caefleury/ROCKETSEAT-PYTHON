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