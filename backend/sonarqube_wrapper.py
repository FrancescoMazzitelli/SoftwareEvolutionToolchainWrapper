import subprocess
import multiprocessing
import os
import re
import shutil
import time
import signal
import webbrowser

to_analyze = os.path.abspath('To_Analyze')
target_folder = os.path.abspath('tools/sonar-scanner/bin/To_Analyze')
sonar_properties = os.path.abspath('tools/sonar-scanner/bin/sonar-project.properties')
sonar_server_folder = os.path.abspath('tools/sonarqube/bin/windows-x86-64')
sonar_scanner_folder =  os.path.abspath('tools/sonar-scanner/bin')

def set_properties():
    
    """
    Metodo che recupera il file properties presente in sonar-scanner,
    se non esiste lo crea, preleva automaticamente il sorgente da
    analizzare e salva sul documento tutte le  informazioni di cui
    sonar-scanner ha bisogno per analizzare il progetto scaricato
    :return: file .properties
    """
    root_to_remove = sonar_scanner_folder[0]
    copy = re.sub(':', '', sonar_scanner_folder)
    copy.replace('\\', '/')
    copy.replace(root_to_remove, '')

    if os.path.isfile(sonar_properties) == False:
        open(sonar_properties, "x")

    prop = open(sonar_properties, "w+")
    
    prop.write("sonar.projectKey=To_Analyze"+"\n")
    prop.write("sonar.projectName=To_Analyze"+"\n")
    prop.write("sonar.sources={}".format(copy)+"\n")
    prop.write("sonar.java.binaries=."+"\n")
    prop.write("sonar.scm.disabled=true"+"\n")

    prop.close()

def move_project_to_analyze():
    
    """
    Metodo che si occupa di effettuare un'operazione di copia
    del progetto da analizzare in una cartella target:
    sonar-scanner/bin/ToAnalyze
    """
    
    if os.path.exists(target_folder) == False:
        shutil.copyfile(to_analyze, target_folder)

def start_sonar_server():
    
    """
    Metodo adibito all'esecuzione del server sonarqube. Viene 
    utilizzato un sottoprocesso per sfruttare le chiamate al
    sistema operativo per l'esecuzione dei file .bat
    """
    os.chdir(sonar_server_folder)
    subprocess.run('StartSonar.bat')

def start_sonar_scanner(wait):
    
    """
    Metodo adibito all'esecuzione del client sonar-scanner.
    utilizzato un sottoprocesso per sfruttare le chiamate al
    sistema operativo per l'esecuzione dei file .bat. La
    variabile wait contiene il valore in secondi che bisogna
    aspettare affinchè il flow of event sia correttamente
    sincronizzato
    :param wait: parametro contenente un valore di tempo in
    secondi
    """
    
    time.sleep(wait)
    os.chdir(sonar_scanner_folder)
    subprocess.run('sonar-scanner.bat')

def stop_sonar_scanner(process, wait):

    """
    Metodo adibito allo stop del client sonar-scanner.
    Tramite una chiamata al sistema operativo viene 
    simulato un segnale  generato dalla sequenza di
    tasti CTRL+C in modo da forzare l'arresto del
    client. 
    :param process: processo da arrestare
    :param wait: parametro contenente un valore di tempo 
    in secondi
    """
    
    time.sleep(wait)
    os.kill(process, signal.CTRL_C_EVENT)

def show_results_in_browser(wait):

    """
    Metodo adibito all'apertura del browser contrassegnato
    come "predefinito" nell'ambiente software in cui è 
    immerso il modulo; e all'apertura di una nuova finestra
    che mostra la dashoboard del server sonarqube, contenente
    i risultati.
    :param wait: parametro contenente un valore di tempo 
    in secondi
    """
    
    time.sleep(wait)
    webbrowser.open_new_tab('http://localhost:9000/dashboard?id=To_Analyze')

def sonar():

    """
    Metodo che definisce il flow of events del modulo wrapper
    sonarqube. Questo prevede l'utilizzo del multiprocessing
    di python in modo da poter effettuare chiamate a
    sottoprocessi parallelamente. Vengono creati i processi
    attribuendo ad ognuno di essi un metodo specifico, vengono
    fatti partire e salvati all'interno di una lista. La lista
    viene poi iterata ed effettuato il "join" di ogni processo
    per esecuzioni parallele
    """
    
    processes = []
    set_properties()
    move_project_to_analyze()
    p1 = multiprocessing.Process(target=start_sonar_server)
    p2 = multiprocessing.Process(target=start_sonar_scanner, args=[70]) #1 minuto e 10 secondi dopo p1
    p3 = multiprocessing.Process(target=stop_sonar_scanner, args=[p2, 670]) #10 minuti dopo p2
    p4 = multiprocessing.Process(target=show_results_in_browser, args=[730]) #1 minuto dopo p3

    p4.start()
    p3.start()
    p2.start()
    p1.start()

    processes.append(p4)
    processes.append(p3)
    processes.append(p2)
    processes.append(p1)

    for process in processes:
        process.join()

    