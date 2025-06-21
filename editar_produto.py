import base, exibir_produtos

def alterar() -> None:
    
    exibir_produtos.exibir_produtos()
    if not base.listagem: return

    alternativa = alternativa - 1

    if alternativa_item == 1:
        base.listagem[alternativa].nome = alternativa_alterada
        print(f"{base.listagem[alternativa].nome} alterado com sucesso na sua lista!")
        return

    elif alternativa_item == 2:
        base.listagem[alternativa].sku = alternativa_alterada
        print(f"{base.listagem[alternativa].sku} alterado com sucesso na sua lista!")
        return

    elif alternativa_item == 3:
        base.listagem[alternativa].cod_barras = int(alternativa_alterada)
        print(f"{base.listagem[alternativa].cod_barras}  alterado com sucesso na sua lista!")
        return
    
    elif alternativa_item == 4:
        base.listagem[alternativa].peso = float(alternativa_alterada)
        print(f"Peso alterado com sucesso para {base.listagem[alternativa].peso} KG!")
    
    elif alternativa_item == 5:
        base.listagem[alternativa].valor_compra = float(alternativa_alterada)
        print(f"Valor de compra alterado com sucesso para R$ {base.listagem[alternativa].valor_compra}!")
    
    elif alternativa_item == 6:
        base.listagem[alternativa].valor_final = float(alternativa_alterada)
        print(f"Valor de venda alterado com sucesso para R$ {base.listagem[alternativa].valor_final}!")
    
    elif alternativa_item == 7:
        base.listagem[alternativa].quantidade = int(alternativa_alterada)
        print(f"Quantidade alterada com sucesso para {base.listagem[alternativa].quantidade} unidades!")

    else: print("Opção inválida. Tente novamente!")
    return

if __name__ == "__main__":

    while True:
        alternativa = int(input("Qual item você deseja alterar?: "))
        alternativa_item = int(input("1. Alterar NOME \n 2. Alterar SKU \n 3. Alterar CÓDIGO DE BARRAS \n" \
        "4. Alterar PESO \n 5. Alterar VALOR DE COMPRA \n 6. Alterar VALOR DE VENDA \n 7. Alterar QUANTIDADE \n" \
        " Digite qual opção deseja alterar: "))
        alternativa_alterada = input("Digite o novo valor para alterar: ")
    