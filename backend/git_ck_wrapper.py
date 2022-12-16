from pydriller import Repository
import subprocess
import git
import json
import os

setting = open("settings.json")
settings = json.load(setting)
remote_repo = settings['repo']
branch = settings['branch']

local_repo_path = "To_Analyze"

def clone_repo():
    subprocess.call(['git', 'clone', remote_repo, local_repo_path])

def checkout_repo():
    subprocess.call(['git', 'checkout', 'release-2.x'])

def print_current_branch(repo):
    branch = repo.active_branch
    print(branch)

def repo_to_use():
    repo = Repository(local_repo_path)
    return repo 

def get_repo_by_local_path(repo_path):
    repo = git.Repo(repo_path)
    return repo 

def get_commits(repo):
    git_commits = repo.traverse_commits()
    return git_commits

def __filter_by_authors(git_commits):
    filtered_commits = []
    authors = []
    
    for commit in git_commits:
        if commit.committer.name not in authors:
            authors.append(commit.committer.name)
            filtered_commits.append(commit)
    return filtered_commits

def __filter_by_year(git_commits):
    filtered_commits = []
    years = []

    for commit in git_commits:
        year = commit.committer_date.year
        if year not in years:
            years.append(year)
            filtered_commits.append(commit)
    return filtered_commits

def print_commits(commits):
    for commit in commits:
        print("Committed by %s on %s with sha %s" % (commit.committer.name, commit.committer_date, commit.hash))

def author_ck_metrics(git_commits):
    to_analyze = os.path.abspath('To_Analyze')
    ck_tool = os.path.abspath('ck.jar')
    filtered_commits = __filter_by_authors(git_commits)
    for commit in filtered_commits:
        os.chdir(to_analyze)
        subprocess.call(['git', 'checkout', commit.hash])
        print("+------------------------------------------------------------------------CHECKOUT TERMINATO")
        os.chdir(os.path.dirname(ck_tool))
        subprocess.call(['java', '-jar', 'ck.jar', local_repo_path, 'false', '0', 'true', "output/{} ".format(commit.committer.name)])
        print("+------------------------------------------------------------------------CK-TOOL TERMINATO")

def year_ck_metrics(git_commits):
    to_analyze = os.path.abspath('To_Analyze')
    ck_tool = os.path.abspath('ck.jar')
    filtered_commits = __filter_by_year(git_commits)
    for commit in filtered_commits:
        os.chdir(to_analyze)
        subprocess.call(['git', 'checkout', '-f', commit.hash])
        print("+------------------------------------------------------------------------CHECKOUT TERMINATO")
        os.chdir(os.path.dirname(ck_tool))
        subprocess.call(['java', '-jar', 'ck.jar', to_analyze, 'false', '0', 'true', "output/{} ".format(commit.committer_date.year)])
        print("+------------------------------------------------------------------------CK-TOOL TERMINATO")

def delete_unnecessary(file_to_keep):
    for filename in os.listdir("output"):
        if not file_to_keep in filename:
            os.remove("output/"+filename)