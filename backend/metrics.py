import pandas as pd
import glob

path = "output"
all_files = glob.glob(path + "/*.csv")

def cbo_average():
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["cbo"].mean()
        li.append(average)

    return li

def cbo_modified_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["cboModified"].mean()
        li.append(average)

    return li
    
def fan_in_average():
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["fanin"].mean()
        li.append(average)

    return li

def fan_out_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["fanout"].mean()
        li.append(average)

    return li

def dit_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["dit"].mean()
        li.append(average)

    return li

def noc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["noc"].mean()
        li.append(average)

    return li

def wmc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["wmc"].mean()
        li.append(average)

    return li

def rfc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["rfc"].mean()
        li.append(average)

    return li

def nosi_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["nosi"].mean()
        li.append(average)

    return li

def loc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["loc"].mean()
        li.append(average)

    return li

def lcom_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcom"].mean()
        li.append(average)

    return li

def lcom_star_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcom*"].mean()
        li.append(average)

    return li

def tcc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["tcc"].mean()
        li.append(average)

    return li

def lcc_average():
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=",")
        average = df["lcc"].mean()
        li.append(average)

    return li
