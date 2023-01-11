import pandas as pd
import glob
import numpy as np

path = "output"
all_files = glob.glob(path + "/*.csv")

def metric_average(metric):

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media di tutte le metriche per ogni commit
    :return: lista di tutte le metriche per commit
    """
    
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        if metric == "lcom" and df[metric][0] > 100:
            df.drop(index=df.index[0], axis=0, inplace=True)            
            average = np.nanmean(df[metric])
            li.append(average)
        else:
            average = np.nanmean(df[metric])
            li.append(average)

    return li
