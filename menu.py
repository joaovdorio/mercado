import cadastrar_produto, editar_produto, exibir_produtos

while True:
    print("Bem vindo ao menu do mercado!")
    print("1. Cadastrar produto \n2. Editar produto\n 3. Exibir produtos")
    opcao = opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_produto.cadastrar()

    if opcao == 2:
        editar_produto.alterar()

    if opcao == 3:
        exibir_produtos.exibir_produtos()
