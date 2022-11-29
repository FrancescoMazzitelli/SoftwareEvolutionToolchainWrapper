import subprocess
import git
import time
import json
import os

setting = open("settings.json")
settings = json.load(setting)
remote_repo = settings['repo']
branch = settings['branch']

local_repo_path = "To_Analyze"

def config_git_bash():
    #subprocess.Popen(['runas', '/noprofile', '/user:Administrator', 'CMD.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(['git', 'config', '--system', 'core.longpaths', 'true'])

def clone_repo():
    #git.Repo.clone_from(remote_repo, 'To_Analyze')
    subprocess.call(['git', 'clone', remote_repo, local_repo_path])

def checkout_repo():
    subprocess.call(['git', 'checkout', 'release-2.x'])

def print_current_branch(repo):
    branch = repo.active_branch
    print(branch)

def repo_to_use():
    repo = git.Repo(local_repo_path)
    return repo 

def get_repo_by_local_path(repo_path):
    repo = git.Repo(repo_path)
    return repo 

def get_commits(repo):
    git_commits = repo.iter_commits('--all')
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
        year = time.strftime("%Y", time.localtime(commit.committed_date))
        if year not in years:
            years.append(year)
            filtered_commits.append(commit)
    return filtered_commits

def print_commits(commits):
    for commit in commits:
        print("Committed by %s on %s with sha %s" % (commit.committer.name, time.strftime("%a, %d %b %Y %H:%M", time.localtime(commit.committed_date)), commit.hexsha))

def author_ck_metrics(git_commits):
    absolute_path = os.path.abspath('To_Analyze')
    filtered_commits = __filter_by_authors(git_commits)
    for commit in filtered_commits:
        subprocess.call(['git', 'checkout', commit.hexsha, absolute_path])
        subprocess.call(['java', '-jar', 'ck.jar', local_repo_path, 'false', '0', 'true', "output/{} ".format(commit.committer.name)])

def year_ck_metrics(git_commits):
    filtered_commits = __filter_by_year(git_commits)
    absolute_path = os.path.abspath('To_Analyze')
    for commit in filtered_commits:
        subprocess.call(['git', 'checkout', commit.hexsha, absolute_path])
        subprocess.call(['java', '-jar', 'ck.jar', local_repo_path, 'false', '0', 'true', "output/{} ".format(time.strftime("%Y", time.localtime(commit.committed_date)))])

def delete_unnecessary(file_to_keep):
    for filename in os.listdir("output"):
        if not file_to_keep in filename:
            os.remove("output/"+filename)