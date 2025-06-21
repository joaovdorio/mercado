import base, exibir_produtos

def excluir():
    base.listagem.pop(opcao)
    print("Item excluido com sucesso")
    print(f"Listagem atualizada de produtos: \n {base.listagem}")
    return

if __name__ == "__main__":
    
    while True:
        exibir_produtos.exibir_produtos()
        opcao = input("Qual item deseja apagar?")
        opcao -= int(opcao)
        excluir()   