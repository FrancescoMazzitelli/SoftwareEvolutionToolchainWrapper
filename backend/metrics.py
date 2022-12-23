import pandas as pd
import glob
import numpy as np

path = "output"
all_files = glob.glob(path + "/*.csv")

def cbo_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica CBO per ogni commit
    :return: lista di tutte le metriche CBO per commit
    """
    
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["cbo"].mean()
        average = np.nanmean(df["cbo"])
        li.append(average)

    return li

def cbo_modified_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica CBO_MODIFIED per ogni commit
    :return: lista di tutte le metriche CBO_MODIFIED per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["cboModified"].mean()
        average = np.nanmean(df["cboModified"])
        li.append(average)

    return li
    
def fan_in_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica FAN-IN per ogni commit
    :return: lista di tutte le metriche FAN-IN per commit
    """

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["fanin"].mean()
        average = np.nanmean(df["fanin"])
        li.append(average)

    return li

def fan_out_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica FAN-OUT per ogni commit
    :return: lista di tutte le metriche FAN-OUT per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["fanout"].mean()
        #average = df["fanout"].nanmean()
        li.append(average)

    return li

def dit_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica DIT per ogni commit
    :return: lista di tutte le metriche DIT per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["dit"].mean()
        average = np.nanmean(df["dit"])
        li.append(average)

    return li

def noc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica NOC per ogni commit
    :return: lista di tutte le metriche NOC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["noc"].mean()
        average = np.nanmean(df["noc"])
        li.append(average)

    return li

def wmc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica WMC per ogni commit
    :return: lista di tutte le metriche WMC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["wmc"].mean()
        average = np.nanmean(df["wmc"])
        li.append(average)

    return li

def rfc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica RFC per ogni commit
    :return: lista di tutte le metriche RFC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["rfc"].mean()
        average = np.nanmean(df["rfc"])
        li.append(average)

    return li

def nosi_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica NOSI per ogni commit
    :return: lista di tutte le metriche NOSI per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["nosi"].mean()
        average = np.nanmean(df["nosi"])
        li.append(average)

    return li

def loc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica LOC per ogni commit
    :return: lista di tutte le metriche LOC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["loc"].mean()
        average = np.nanmean(df["loc"])
        li.append(average)

    return li

def lcom_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica LCOM per ogni commit
    :return: lista di tutte le metriche LCOM per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcom"].mean()
        average = np.nanmean(df["lcom"])
        li.append(average)

    return li

def lcom_star_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica LCOM* per ogni commit
    :return: lista di tutte le metriche LCOM* per commit
    """


    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcom*"].mean()
        average = np.nanmean(df["lcom*"])
        li.append(average)

    return li

def tcc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica TCC per ogni commit
    :return: lista di tutte le metriche TCC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["tcc"].mean()
        average = np.nanmean(df["tcc"])
        li.append(average)

    return li

def lcc_average():

    """
    Metodo che legge tutti i file csv e ritorna una lista
    contenente la media della metrica LCC per ogni commit
    :return: lista di tutte le metriche LCC per commit
    """

    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcc"].mean()
        average = np.nanmean(df["lcc"])
        li.append(average)

    return li
