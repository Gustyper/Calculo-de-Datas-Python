import numpy as np
import pandas as pd

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def calculo_digita(data):
    array =  np.char.split(data, sep="-", maxsplit=2)
    df = pd.Series(array)
    print(df)
    pass

def calculo_arquivo(data):
    pass