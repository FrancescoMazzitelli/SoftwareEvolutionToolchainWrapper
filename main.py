import backend.git_ck_wrapper as git_ck
import backend.nicad_wrapper as nicad
import backend.sonarqube_wrapper  as sonar
import analysis
from xml.dom import minidom
import os

folder = "To_Analyze"

def check_repo():

    """
    Metodo che controlla se il progetto da analizzare è presente
    sul file system

    :param folder: path della cartella da controllare
    :return: "clone" del repository sul file system
    """
    
    if os.path.exists(folder):
        content = os.listdir(folder)
        if content is not None:
            return 0
    else:
        git_ck.clone_repo()

def check_folder():

    """
    Metodo che controlla se la cartella di output è presente
    sul file system

    :return: creazione della cartella "output"
    """
    
    if not os.path.exists("output"):
        path = os.path.join("output")
        os.mkdir(path)

def check_nicad_input():

    """
    Metodo che controlla se la cartella "nicad_input" è presente
    sul file system e ritorna il contenuto della cartella in una 
    lista per la sua succesiva iterazione

    :return: "paths" lista dei file presenti nella cartella di input
    """
    
    paths = []
    file_path = os.path.abspath("nicad_input")
    files = os.listdir(file_path)
    for file in files:
        paths.append("nicad_input/"+file)
    return paths

if __name__ == '__main__':
    
    #-----------------------------------------------INIIAL CHECK----------------//
     
    try:
        check_repo()
        check_folder()
    except:
        print("Warning")
    
    #----------------------------------------------------CK---------------------//

    git_ck.date_ck_metrics()
    #git_ck.all_ck_metrics()
    
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
    #analysis.pie_chart()

    #-------------------------------------------------HISTOGRAM-----------------//
    #analysis.bar_chart()
