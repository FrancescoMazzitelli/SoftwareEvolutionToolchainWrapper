import backend
from prettytable import PrettyTable

metrics_avg_table = PrettyTable([])

def metrics_average():
    cbo_avg = backend.cbo_average()
    cbo_modified_avg = backend.cbo_modified_average()
    fan_in_avg = backend.fan_in_average()
    fan_out_avg = backend.fan_out_average()
    dit_avg = backend.dit_average()
    noc_avg = backend.noc_average()
    loc_avg = backend.loc_average()
    rfc_avg = backend.rfc_average()
    tcc_avg = backend.tcc_average()
    nosi_avg = backend.nosi_average()
    lcom_avg = backend.lcom_star_average()
    lcom_star_avg = backend.lcom_star_average() 
    lcc_avg = backend.lcc_average()
    wmc_avg = backend.wmc_average()

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


