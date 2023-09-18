import numpy as np
import pandas as pd

from datetime import datetime

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

def calculo_arquivo(data):
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_
    """

    pass