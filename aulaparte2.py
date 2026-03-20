class produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def vender(self, quantiaATirar):
        if self.estoque < quantiaATirar:
            print("Estoque insuficiente!")
        else:
            self.estoque = self.estoque - quantiaATirar
    def repor(self, quantiaARepor):
        self.estoque = self.estoque + quantiaARepor
    def exibirDados(self):
        print(self.nome)
        print(self.preco)
        print(self.estoque)
    
produtoAVenda = produto("bola", 19, 47)
produtoAVenda.vender(4)
produtoAVenda.vender(58)
