import backend.git_ck_wrapper as git_ck
import backend.nicad_wrapper as nicad
import backend.sonarqube_wrapper  as sonar
from xml.dom import minidom
import analysis
import os

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
    
if __name__ == '__main__':
    
    #-----------------------------------------------INIIAL CHECK----------------//
     
    try:
        check_repo()
        check_folder()
    except:
        print("Warning")
    
    #----------------------------------------------------CK---------------------//
    #repo = git_ck.repo_to_use()
    #git_commits = git_ck.get_commits(repo)
    #git_ck.all_ck_metrics(git_commits)
    
    #git_ck.delete_unnecessary(file_to_keep="class")

    #analysis.metrics_average()
    #analysis.graph_plot()
    
    #---------------------------------------------------NICAD-------------------//
    #for file in check_nicad_input():
    #    fileToSend = file.replace("nicad_input/", "")
    #    xml = minidom.parse(file)
    #    nicad.xml_wrapper(fileToSend, xml)

    #-------------------------------------------------SONARQUBE-----------------//
    #sonar.sonar()
    
