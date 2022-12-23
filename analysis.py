import backend.metrics as metrics
from prettytable import PrettyTable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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


def graph_plot():
    
    """
    Metodo adibito al plot automatico di un grafico che mostra
    l'andamento delle metriche nel tempo, in relazione ai commit
    analizzati
    """
    table = read_table()
    for column in table:
        if 'fanout' in column:
            pass
        else:
            y = table[column]
            x = range(0, len(y))
            plt.plot(x, y, label=column)
        
    plt.legend(bbox_to_anchor=(1.4, 0.6), loc='center right')
    plt.tight_layout()
    plt.savefig("figures/andamento metriche nel tempo.png")
    plt.show()

def corr_matrix_plot():
    
    """
    Metodo adibito al plot automatico delle matrici di correlazione
    che mostrano i rapporti di proporzionalità tra le metriche
    """
    
    df = read_table()
    metrics = pd.DataFrame({
    'CBO':df['cbo'],
    'CBOM': df["cboModified"],
    'FAN-I': df["fanin"],
    'DIT': df["dit"],
    'NOC': df["noc"],
    'WMC': df["wmc"],
    'RFC': df["rfc"],
    'NOSI': df["nosi"],
    'LOC': df["loc"],
    'LCOM': df["lcom"],
    'LCOM*': df["lcom*"],
    'TCC': df["tcc"],
    'LCC': df["lcc"]
    })


    corr_df = metrics.corr(method='pearson')

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df, annot=True, cmap="YlGnBu")
    plt.savefig("figures/correlazioniMetriche.png")
    plt.show()

def pie_chart():

    """
    Metodo non automatico adibito alla creazione di un diagramma a
    torta per rappresentare i risultati della clone analysis
    """

    df = pd.DataFrame({'Clones': [0, 2, 0]})
    labels = ['Type-1', 'Type-2', 'Type-3']
    plt.pie(df['Clones'], labels=None, autopct='%1.0f%%')
    plt.legend(labels=labels)
    plt.show()

def bar_chart():

    """
    Metodo non automatico adibito alla creazione di un istogramma per
    rappresentare i risultati dei sintesi delle metriche di progetto
    """
    
    fxgraphics2d = [6.99, 8.14, 1.15, 6.99, 1.74, 0, 25.76, 0.04, 3.40, 0.23, 0.23, 0.07, 20.16]
    commons = [6.04, 8.40, 2.36, 6.04, 1.36, 0.24, 8.90, 0.20, 6.43, 0.20, 0.20, 0.21, 8.34]
    dubbo_samples = [3.62, 4.54, 0.84, 3.70, 1.02, 0.03, 5.96, 0.13, 0.84, 0.16, 0.16, 0.17, 4.65]
    retrofit = [3.82, 5.22, 1.40, 3.82, 1.20, 0.03, 4.06, 0.11, 0.97, 0.11, 0.11, 0.14, 4.41]
    gmaven = [4.87, 6.77, 1.90, 4.87, 1.47, 0.15, 6.88, 0.35, 0.49, 0.22, 0.22, 0.40, 5.05]

    labels = ['cbo', 'cboModified', 'fanin', 'fanout', 'dit', 'noc', 'rfc', 'tcc', 'nosi', 'lcom', 'lcom*', 'lcc', 'wmc']
    bins = np.arange(len(labels))

    plt.bar(bins - 0.3, fxgraphics2d, 0.2, label='fxgraphics2d')
    plt.bar(bins - 0.15, commons, 0.2, label='commons')
    plt.bar(bins, dubbo_samples, 0.2, label='dubbo_samples')
    plt.bar(bins + 0.15, retrofit, 0.2, label='retrofit')
    plt.bar(bins + 0.3, gmaven, 0.2, label='gmaven')
    plt.xticks(bins, labels)
    plt.legend()
    plt.show()