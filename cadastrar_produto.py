##biblioteca de cadastro de produto

import base, exibir_produtos

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

def inputar(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final) -> None: #jogar o cadastro dentro da lista
    produto = Produto(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final)
    base.listagem.append(produto)
    print("Produto cadastrado com sucesso! \n")
    return

 
def cadastrar(): #receber os valores
   while True:
            nome = input("Digite o nome do produto: ")
            sku = input("Digite o SKU do produto: ")
            cod_barras = validar_cod_barras()
            peso = float(input("Digite o peso do produto, em KG: "))
            valor_compra = float(input("Digite o valor de compra do produto: "))
            valor_final = float(input("Digite o valor de venda do produto: "))
            quantidade = int(input("Digite quantos itens serão adicionados em estoque: "))

            inputar(nome, sku, cod_barras, peso, quantidade, valor_compra, valor_final)
            

            continuar = input("Deseja cadastrar outro produto? (S/N)   ")
            if continuar.casefold() != "s":
                print("Produto cadastrado com sucesso!")
                exibir_produtos.exibir_produtos()
                break

def validar_cod_barras():
    while True:
        cod_barras = input("Digite o código de barras (13 dígitos): ")
        if len(cod_barras) == 13:
            return int(cod_barras)
        else:
            print("Código inválido - EAN deve ter 13 dígitos.")


if __name__ == "__main__":

    cadastrar()