import funcoes

input = 0

while input != 3:
    print("MENU")
    print("1 - Digite as datas")
    print("2 - Digite o nome de um arquivo")
    print("3 - Sair")
    
    input = input()

    if input == 1:
        datas = input()
        funcoes.calculo_digita(datas)
    elif input == 2:
        datas = input()
        funcoes.calculo_arquivo(datas)
    elif input != 3:
        print("Digite um numero válido")

