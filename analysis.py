import backend.metrics as metrics
from prettytable import PrettyTable

metrics_avg_table = PrettyTable([])

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

    with open('metrics_avg_table', 'w') as w:
        w.write(str(metrics_avg_table))


