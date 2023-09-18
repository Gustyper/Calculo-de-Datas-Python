import funcoes

opcao = 0

while opcao != 3:

    print("################################################")
    print("MENU")
    print("1 - Digite as datas")
    print("2 - Digite o nome de um arquivo")
    print("3 - Sair")
    
    opcao = input("Digite um número: ")

    try:
        opcao = int(opcao)
    except:
        print("Digite un número inteiro")
        continue

    if opcao == 1:
        datas = input("Digite as datas: ")
        funcoes.calculo_digita(datas)
    elif opcao == 2:
        nome_arquivo = input("Digite o nome do arquivo: ")
        funcoes.calculo_arquivo(nome_arquivo)
    elif opcao != 3:
        print("-------------------------------")
        print("Digite um numero válido")

print("Saindo do programa")