import pandas as pd
from datetime import datetime
import doctest
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

def calculo_digita(data):
    """ Função que calcula o número de dias entre datas dentro de um arquivo texto.

    Parameters
    ----------
    data : string
        Datas no formato especificado "DD de MÊS de ANO - DD de MÊS de ANO"

    Returns
    -------
    int 
        A quantidade de dias entre duas datas

    Teste 1
    >>> calculo_digita("23 de Agosto de 2023 - 18 de Setembro de 2023")
    26

    Teste 2
    >>> calculo_digita("18 de Setembro de 2023 - 23 de Agosto de 2023")
    26
    """
    
    #Separa as datas
    array = data.split(" - ")

    #Formata em datetime
    data1 = datetime.strptime(array[0], "%d de %B de %Y")
    data2 = datetime.strptime(array[1], "%d de %B de %Y")

    numero_dias = abs((data2 - data1).days)

    print(numero_dias)


def calculo_arquivo(file_name):
    """ Função que calcula o número de dias entre datas dentro de um arquivo texto.

    Parameters
    ----------
    file_name : string
        Nome do arquivo recebido no input.

    Returns 
    -------
    int
        Retorna a quantidade de dias entre as datas.
    """
    try:
        dados = pd.read_csv(file_name, sep=" - ", header=None, names=["Coluna1", "Coluna2"], engine='python')

        if not dados.empty:
            primeira_data = dados.iloc[0, 0]
            segunda_data = dados.iloc[0, 1]
           
            primeira_data = datetime.strptime(primeira_data, '%d de %B de %Y')
            segunda_data = datetime.strptime(segunda_data, '%d de %B de %Y')

            quantidade_dias = abs((segunda_data - primeira_data).days)

            print(quantidade_dias)
        else:
            print("O arquivo está vazio!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio ou não contém dados válidos.")

if __name__ == "__main__":
    doctest.testmod(verbose=True)