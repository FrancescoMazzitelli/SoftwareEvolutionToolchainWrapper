import backend.metrics as metrics
from prettytable import PrettyTable
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

metrics_avg_table = PrettyTable([])
table_from_file = PrettyTable([])

def metrics_average():
    cbo_avg = metrics.cbo_average()
    cbo_modified_avg = metrics.cbo_modified_average()
    fan_in_avg = metrics.fan_in_average()
    fan_out_avg = metrics.fan_out_average()
    dit_avg = metrics.dit_average()
    noc_avg = metrics.noc_average()
    loc_avg = metrics.loc_average()
    rfc_avg = metrics.rfc_average()
    tcc_avg = metrics.tcc_average()
    nosi_avg = metrics.nosi_average()
    lcom_avg = metrics.lcom_star_average()
    lcom_star_avg = metrics.lcom_star_average() 
    lcc_avg = metrics.lcc_average()
    wmc_avg = metrics.wmc_average()

    metrics_avg_table.add_column("cbo", cbo_avg)
    metrics_avg_table.add_column("cboModified", cbo_modified_avg)
    metrics_avg_table.add_column("fanin", fan_in_avg)
    metrics_avg_table.add_column("fanout",fan_out_avg)
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

    with open('metrics_avg_table.csv', 'w') as w:
        w.write(metrics_avg_table.get_csv_string())

def read_table():
    table_from_file = pd.read_csv('metrics_avg_table.csv', sep=',')
    return table_from_file


def graph_plot():
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
    table = read_table()
    df = table
    metrics = pd.DataFrame({
    'CBO':df['cbo'],
    'CBOM': df["cboModified"],
    'FAN-I': df["fanin"],
    #'FAN-O': df["fanout"],
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
