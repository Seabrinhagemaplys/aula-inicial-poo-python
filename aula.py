class pessoa:
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
    def apresentar(self):
        print(self.nome)
        print(self.idade)
        print(self.nacionalidade)
    def fazerAniversario(self):
        self.idade = pessoa.idade + 1
    

pessoa1 = pessoa("Arthur", 19, "Brasileiro")
pessoa2 = pessoa("Lucas", 20, "Canadense")
