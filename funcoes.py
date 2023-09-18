import numpy as np
import pandas as pd
import fileinput
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calculo_digita(data):
    array =  np.char.split(data, sep="-", maxsplit=2)
    df = pd.Series(array)
    print(df)
    pass

def calculo_arquivo():
    
    file_name = input("Digite o nome do arquivo: ")

    try:
        dados = pd.read_csv(file_name, sep=" ", header=None, names=["Coluna1", "Coluna2"])

        if not dados.empty:
            primeira_data = dados.iloc[0, 0]
            segunda_data = dados.iloc[0, 1]
            print(primeira_data,segunda_data)
        else:
            print("O arquivo está vazio!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio ou não contém dados válidos.")

calculo_arquivo()