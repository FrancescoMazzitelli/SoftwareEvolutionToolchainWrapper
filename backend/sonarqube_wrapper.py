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
    root_to_remove = sonar_scanner_folder[0]
    copy0 = re.sub(':', '', sonar_scanner_folder)
    copy1 = copy0.replace('\\', '/')
    copy = copy1.replace(root_to_remove, '')

    if os.path.isfile(sonar_properties) == False:
        f = open(sonar_properties, "x")

    prop = open(sonar_properties, "w+")
    
    p1 = "sonar.projectKey=To_Analyze"
    p2 = "sonar.projectName=To_Analyze"
    p3 = "sonar.sources={}".format(copy)
    p4 = "sonar.java.binaries=."
    p5 = "sonar.scm.disabled=true"

    prop.write(p1+"\n")
    prop.write(p2+"\n")
    prop.write(p3+"\n")
    prop.write(p4+"\n")
    prop.write(p5+"\n")

    prop.close()

def move_project_to_analyze():
    if os.path.exists(target_folder) == False:
        shutil.copyfile(to_analyze, target_folder)

def start_sonar_server():
    os.chdir(sonar_server_folder)
    subprocess.run('StartSonar.bat')

def start_sonar_scanner(wait):
    time.sleep(wait)
    os.chdir(sonar_scanner_folder)
    subprocess.run('sonar-scanner.bat')

def stop_sonar_scanner(process, wait):
    time.sleep(wait)
    os.kill(process, signal.CTRL_C_EVENT)

def show_results_in_browser(wait):
    time.sleep(wait)
    url = 'http://localhost:9000/dashboard?id=To_Analyze'
    webbrowser.open_new_tab(url)

def sonar():
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

    