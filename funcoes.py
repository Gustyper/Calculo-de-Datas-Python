import numpy as np
import pandas as pd

from datetime import datetime
import fileinput
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calculo_digita(data):
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_


    """

    array = data.split(" - ")
    print(array[0])

    data1 = datetime.strptime(array[0], "%d de %B de %Y")
    data2 = datetime.strptime(array[1], "%d de %B de %Y")

    print((data2 - data1).days)


def calculo_arquivo(file_name):

    try:
        dados = pd.read_csv(file_name, sep=" ", header=None, names=["Coluna1", "Coluna2"])

        if not dados.empty:
            primeira_data = dados.iloc[0, 0]
            segunda_data = dados.iloc[0, 1]
           
            primeira_data = datetime.strptime(primeira_data, '%Y/%m/%d')
            segunda_data = datetime.strptime(segunda_data, '%Y/%m/%d')

            quantidade_dias = abs((segunda_data - primeira_data).days)

            print(quantidade_dias)
        else:
            print("O arquivo está vazio!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio ou não contém dados válidos.")