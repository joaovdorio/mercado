##biblioteca de cadastro de produto

import base, functions

class Produto:
    def __init__(self, nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final):
        self.nome = nome
        self.sku = sku
        self.cod_barras = cod_barras
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_final = valor_final
        self.quantidade = quantidade
        return

def cadastrar(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final) -> None:
    produto = Produto(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final)
    base.listagem.append(produto)
    print("Produto cadastrado com sucesso! \n")
    return

while True:
    nome = input("Digite o nome do produto: ")
    sku = input("Digite o SKU do produto: ")
    cod_barras = int(input("Digite o código de barras (13 dígitos): "))
    peso = float(input("Digite o peso do produto, em KG: "))
    valor_compra = float(input("Digite o valor de compra do produto: "))
    valor_final = float(input("Digite o valor de venda do produto: "))
    quantidade = int(input("Digite quantos itens serão adicionados em estoque: "))

    cadastrar(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final)
    
    continuar = input("Deseja cadastrar outro produto? (S/N)   ")
    if continuar.casefold() != "s":
        break
    else: print("Produto cadastrado com sucesso!")
    functions.exibir_produtos()


