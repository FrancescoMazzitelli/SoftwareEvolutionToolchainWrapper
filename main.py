import backend.git_ck_wrapper as git_ck
import matplotlib.pyplot as plt 
import pandas as pd
import backend.nicad_wrapper as nicad
import backend.sonarqube_wrapper  as sonar
from xml.dom import minidom
import analysis
import os
import numpy as np

folder = "To_Analyze"

def check_repo():
    if os.path.exists(folder):
        content = os.listdir(folder)
        if content is not None:
            return 0
    else:
        git_ck.clone_repo()

def check_folder():
    if not os.path.exists("output"):
        path = os.path.join("output")
        os.mkdir(path)

def check_nicad_input():
    paths = []
    file_path = os.path.abspath("nicad_input")
    files = os.listdir(file_path)
    for file in files:
        paths.append("nicad_input/"+file)
    return paths

def pie_chart():
    df = pd.DataFrame({'Clones': [0, 2, 0]})
    labels = ['Type-1', 'Type-2', 'Type-3'] #
    #plot = df.plot.pie(y='Clones', figsize=(5, 5))
    plt.pie(df['Clones'], labels=None, autopct='%1.0f%%')
    plt.legend(labels=labels)
    plt.show()

def bar_chart():
    
    fig, ax = plt.subplots()

    fxgraphics2d = [6.99, 8.14, 1.15, 6.99, 1.74, 0, 25.76, 0.04, 3.40, 0.23, 0.23, 0.07, 20.16]
    commons = [6.04, 8.40, 2.36, 6.04, 1.36, 0.24, 8.90, 0.20, 6.43, 0.20, 0.20, 0.21, 8.34]
    dubbo_samples = [3.62, 4.54, 0.84, 3.70, 1.02, 0.03, 5.96, 0.13, 0.84, 0.16, 0.16, 0.17, 4.65]
    retrofit = [3.82, 5.22, 1.40, 3.82, 1.20, 0.03, 4.06, 0.11, 0.97, 0.11, 0.11, 0.14, 4.41]
    gmaven = [4.87, 6.77, 1.90, 4.87, 1.47, 0.15, 6.88, 0.35, 0.49, 0.22, 0.22, 0.40, 5.05]

    labels = ['cbo', 'cboModified', 'fanin', 'fanout', 'dit', 'noc', 'rfc', 'tcc', 'nosi', 'lcom', 'lcom*', 'lcc', 'wmc']
    bins = np.arange(len(labels))
    #xticks = [i for i in range(14)]
    #plt.bar([fxgraphics2d, commons, dubbo_samples, retrofit, gmaven], bins, label=['fxgraphics2d', 'commons', 'dubbo_samples', 'retrofit', 'gmaven'])
    plt.bar(bins - 0.3, fxgraphics2d, 0.2, label='fxgraphics2d')
    plt.bar(bins - 0.15, commons, 0.2, label='commons')
    plt.bar(bins, dubbo_samples, 0.2, label='dubbo_samples')
    plt.bar(bins + 0.15, retrofit, 0.2, label='retrofit')
    plt.bar(bins + 0.3, gmaven, 0.2, label='gmaven')
    plt.xticks(bins, labels)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    
    #-----------------------------------------------INIIAL CHECK----------------//
     
    try:
        check_repo()
        check_folder()
    except:
        print("Warning")
    
    #----------------------------------------------------CK---------------------//
    repo = git_ck.repo_to_use()
    git_commits = git_ck.get_commits(repo)

    git_ck.date_ck_metrics(git_commits)
    git_ck.all_ck_metrics(git_commits)
    
    git_ck.delete_unnecessary(file_to_keep="class")

    analysis.metrics_average()

    analysis.graph_plot()
    analysis.corr_matrix_plot()
    
    #---------------------------------------------------NICAD-------------------//
    for file in check_nicad_input():
        fileToSend = file.replace("nicad_input/", "")
        xml = minidom.parse(file)
        nicad.xml_wrapper(fileToSend, xml)

    #-------------------------------------------------SONARQUBE-----------------//
    sonar.sonar()

    #-------------------------------------------------PIE-CHART-----------------//
    pie_chart()

    #-------------------------------------------------HISTOGRAM-----------------//
    bar_chart()
