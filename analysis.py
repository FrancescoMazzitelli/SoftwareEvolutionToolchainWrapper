import pandas as pd
import glob
from IPython.display import display
from prettytable import PrettyTable
import dataframe_image as dfi


path = r"C:/Users/donat/OneDrive/Desktop/Progetto-evoluzione-qualita-del-Software/output"
all_files = glob.glob(path + "/*.csv")

metrics_avg_table = PrettyTable([])

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

def metrics_average():
    cbo_avg = cbo_average()
    cbo_modified_avg = cbo_modified_average()
    fan_in_avg = fan_in_average()
    fan_out_avg = fan_out_average()
    dit_avg = dit_average()
    noc_avg = noc_average()
    loc_avg = loc_average()
    rfc_avg = rfc_average()
    tcc_avg = tcc_average()
    nosi_avg = nosi_average()
    lcom_avg = lcom_star_average()
    lcom_star_avg = lcom_star_average() 
    lcc_avg = lcc_average()
    wmc_avg = wmc_average()

    metrics_avg_table.add_column("cbo", cbo_avg)
    metrics_avg_table.add_column("cbo_modified", cbo_modified_avg)
    metrics_avg_table.add_column("fan_in", fan_in_avg)
    metrics_avg_table.add_column("fan_out",fan_out_avg)
    metrics_avg_table.add_column("dit", dit_avg)
    metrics_avg_table.add_column("noc", noc_avg)
    metrics_avg_table.add_column("loc", loc_avg)
    metrics_avg_table.add_column("rfc", rfc_avg)
    metrics_avg_table.add_column("tcc", tcc_avg)
    metrics_avg_table.add_column("nosi", nosi_avg)
    metrics_avg_table.add_column("lcom", lcom_avg)
    metrics_avg_table.add_column("lcom*", lcom_star_avg)
    metrics_avg_table.add_column("lcc", lcc_avg)
    metrics_avg_table.add_column("wmc", wmc_avg)

    #dfi.export(metrics_avg_table, "table.png")
    print(metrics_avg_table)

    


