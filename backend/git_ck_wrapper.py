from pydriller import Repository
import subprocess
import git
import json
import os

setting = open("settings.json")
settings = json.load(setting)
remote_repo = settings['repo']

local_repo_path = "To_Analyze"

def clone_repo():

    """
    Metodo che effettua il clone di un repository target.
    Viene chiamato un sottoprocesso, dipendente dal sistema
    operativo ma le cui modifiche non vengono propagate
    all'intero ambiente, che a sua volta richiama la funzione
    di git da linea di comando
    """

    subprocess.call(['git', 'clone', remote_repo, local_repo_path])

def print_current_branch(repo):
    
    """
    Metodo di debug che mostra il nome del branch attivo
    :param repo: oggetto repository 
    :return: stampa a schermo del branch attivo
    """

    print(repo.active_branch)

def repo_to_use():

    """
    Metodo che restituisce un oggetto Repository creato
    grazie al recupero del path del repository da analizzare
    salvato in locale
    :return: oggetto repository
    """

    return Repository(local_repo_path) 

def get_commits(repo):

    """
    Metodo che restituisce la lista di tutti i commits associati
    ad un repository
    :param repo: oggetto repository
    :return: git_commits, lista dei commits
    """

    return repo.traverse_commits()

def __filter_by_authors(git_commits):

    """
    Metodo che filtra i commit andandone a prendere uno per ogni autore
    
    :param git_commits: La lista di tutti i commit
    :return: La lista dei commit ottenuti applicando il filtro
    """

    filtered_commits = []
    authors = []
    
    for commit in git_commits:
        if commit.committer.name not in authors:
            authors.append(commit.committer.name)
            filtered_commits.append(commit)
    return filtered_commits

def __filter_by_year(git_commits):

    """
    Metodo che filtra i commit andandone a prendere uno per ogni anno
    
    :param git_commits: La lista di tutti i commit
    :return: La lista dei commit ottenuti applicando il filtro
    """

    filtered_commits = []
    years = []

    for commit in git_commits:
        year = commit.committer_date.year
        if year not in years:
            years.append(year)
            filtered_commits.append(commit)
    return filtered_commits


def __filter_by_date(git_commits):

    """
    Metodo che filtra i commit andandone a prendere uno per ogni mese per ogni anno
    
    :param git_commits: La lista di tutti i commit
    :return: La lista dei commit ottenuti applicando il filtro
    """

    filtered_commits = []
    dates = []

    for commit in git_commits:
        date = str(commit.committer_date.month)+str(commit.committer_date.year)
        if date not in dates:
            dates.append(date)
            filtered_commits.append(commit)

    #rimozione del primo commit perchè di solito non contiene codice
    #è solo la creazione del repository
    filtered_commits.remove(filtered_commits[0]) 

    return filtered_commits

def print_commits(commits):

    """
    Metodo di dubug adibito alla stampa a schermo dei commit
    :param commits: lista di commit da stampare
    :return: stampa a schermo dei commit
    """
    for commit in commits:
        print("Committed by %s on %s with sha %s" % (commit.committer.name, commit.committer_date, commit.hash))

def year_ck_metrics():

    """
    Metodo che estrae le metriche ck dalla lista dei commit filtrati per anno e le salva in un csv
    
    :param git_commits: La lista di tutti i commit
    """
    
    to_analyze = os.path.abspath('To_Analyze')
    ck_tool = os.path.abspath('ck.jar')
    
    for commit in __filter_by_year(get_commits(repo_to_use())):
        os.chdir(to_analyze)
        subprocess.call(['git', 'checkout', '-f', commit.hash])
        print("+------------------------------------------------------------------------CHECKOUT TERMINATO")
        os.chdir(os.path.dirname(ck_tool))
        subprocess.call(['java', '-jar', 'ck.jar', to_analyze, 'false', '0', 'true', "output/{} ".format(commit.committer_date.year)])
        print("+------------------------------------------------------------------------CK-TOOL TERMINATO")

def date_ck_metrics():

    """
    Metodo che estrae le metriche ck dalla lista dei commit filtrati per mese e anno e le salva in un csv
    
    :param git_commits: La lista di tutti i commit
    """

    to_analyze = os.path.abspath('To_Analyze')
    ck_tool = os.path.abspath('ck.jar')

    for commit in __filter_by_date(get_commits(repo_to_use())):
        os.chdir(to_analyze)
        subprocess.call(['git', 'checkout', '-f', commit.hash])
        print("+------------------------------------------------------------------------CHECKOUT TERMINATO")
        os.chdir(os.path.dirname(ck_tool))
        subprocess.call(['java', '-jar', 'ck.jar', to_analyze, 'false', '0', 'true', "output/{} ".format(str(commit.committer_date.month)+str(commit.committer_date.year))])
        print("+------------------------------------------------------------------------CK-TOOL TERMINATO")

def all_ck_metrics():
    """
    Metodo che estrae le metriche ck dalla lista di tutti i commit le salva in un csv
    
    :param git_commits: La lista di tutti i commit
    """

    to_analyze = os.path.abspath('To_Analyze')
    ck_tool = os.path.abspath('ck.jar')

    for commit in get_commits(repo_to_use()):
        os.chdir(to_analyze)
        subprocess.call(['git', 'checkout', '-f', commit.hash])
        print("+------------------------------------------------------------------------CHECKOUT TERMINATO")
        os.chdir(os.path.dirname(ck_tool))
        subprocess.call(['java', '-jar', 'ck.jar', to_analyze, 'false', '0', 'true', "output/{} ".format(str(commit.hash))])
        print("+------------------------------------------------------------------------CK-TOOL TERMINATO")

def delete_unnecessary(file_to_keep):
    """
    Metodo che elimina tutti i file non necessari all'analisi del tool ck
    
    :param file_to_keep: La lista dei file da mantenere di tipo class
    """
    for filename in os.listdir("output"):
        if not file_to_keep in filename:
            os.remove("output/"+filename)