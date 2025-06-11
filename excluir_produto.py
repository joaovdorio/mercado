import base, functions

def excluir():
    base.listagem.pop(opcao)
    print("Item excluido com sucesso")
    print(f"Listagem atualizada de produtos: \n {base.listagem}")
    return

if __name__ == "__main__":
    
    while True:
        functions.exibir_produtos()
        opcao = input("Qual item deseja apagar?")
        opcao -= int(opcao)
        excluir()   