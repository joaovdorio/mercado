import base

def exibir_produtos():
    print("Produtos cadastrados: ", len(base.listagem))
    for indice, produto in enumerate(base.listagem, start=1):
        print(f"{indice}. {produto.nome} \n SKU: {produto.sku} \n Código de barras: {produto.cod_barras} \n Peso: {produto.peso}kg \n")
        markup = produto.valor_final / produto.valor_compra if produto.valor_compra != 0 else 0
        print(f"Valor adquirido: R${produto.valor_compra} \n Valor para consumidor: R${produto.valor_final} \n Markup: {markup:.2f}x \n")
        print(f"Quantidade em estoque: {produto.quantidade}")