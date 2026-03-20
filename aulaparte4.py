class Produto:
    def __init__(self, nomeProduto, preco, unidades):
        self.nome = nomeProduto
        self.precoUnitario = preco
        self.quantidade = unidades
    
    def calculeValorEstoque(self):
        return self.quantidade * self.precoUnitario
    
class Loja:
    def __init__(self, nomeLoja):
        self.nome_loja = nomeLoja
    def mostreValorEstoqueProduto(self, produtoACalcular : Produto):
        self.calculo = produtoACalcular.calculeValorEstoque()
        ##print("Na loja", self.nome ,", o valor em estoque do produto", produtoACalcular.nome, "é R$", self.calculo)
        print(f"Na loja {self.nome_loja} o valor em estoque do produto {produtoACalcular.nome} é R$ {self.calculo}")
    
    
produto1 = Produto("Camisa do Galo", 399, 500)
loja1 = Loja("do Galo")

loja1.mostreValorEstoqueProduto(produto1)
