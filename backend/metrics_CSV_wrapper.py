import backend.metrics as metrics
from prettytable import PrettyTable
import pandas as pd

metrics_avg_table = PrettyTable([])
table_from_file = PrettyTable([])
li = ["cbo", "cboModified", "fanin", "dit", "noc", "loc", "rfc", "tcc", "nosi", "lcom", "lcom*", "lcc", "wmc"]


def metrics_average():
    """
    Metodo che richiama quanto definito nel modulo "metrics" e
    genera una tabella "PrettyTable". Dopo aver generato le
    metriche per commit, e quindi la tabella, quest'ultima 
    viene salvata sul file system in un file CSV
    """
    
    for metric in li:
        metrics_avg_table.add_column(metric, metrics.metric_average(metric))

    with open('metrics_avg_table.csv', 'w') as w:
        w.write(metrics_avg_table.get_csv_string())

def read_table():
    
    """
    Metodo che legge la tabella contente le metriche per commit
    e la restituisice

    :return: tabella metriche letta dal file system
    """
    
    return pd.read_csv('metrics_avg_table.csv', sep=',')
