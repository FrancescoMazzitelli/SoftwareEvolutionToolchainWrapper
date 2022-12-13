import pandas as pd
import glob
import numpy as np

path = "output"
all_files = glob.glob(path + "/*.csv")

def cbo_average():
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["cbo"])
        li.append(average)

    return li

def cbo_modified_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["cboModified"])
        li.append(average)

    return li
    
def fan_in_average():
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["fanin"])
        li.append(average)

    return li

'''
def fan_out_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["fanout"].nanmean()
        li.append(average)

    return li
'''

def dit_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["dit"])
        li.append(average)

    return li

def noc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["noc"])
        li.append(average)

    return li

def wmc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["wmc"])
        li.append(average)

    return li

def rfc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["rfc"])
        li.append(average)

    return li

def nosi_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["nosi"])
        li.append(average)

    return li

def loc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["loc"])
        li.append(average)

    return li

def lcom_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["lcom"])
        li.append(average)

    return li

def lcom_star_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["lcom*"])
        li.append(average)

    return li

def tcc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["tcc"])
        li.append(average)

    return li

def lcc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = np.nanmean(df["lcc"])
        li.append(average)

    return li
