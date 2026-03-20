class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def empreste(self):
        print("O livro foi emprestado!")

class Leitor:
    def __init__(self, nome):
        self.nome = nome
    
    def pegueEmprestado(self, livroemprestado):
        livroemprestado.empreste()


livro1 = Livro("Olivrolegal", "Arthur Coronho")
leitor1 = Leitor("Luiza")
leitor1.pegueEmprestado(livro1)

