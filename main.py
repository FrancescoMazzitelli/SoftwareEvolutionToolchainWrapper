import subprocess
import git
import time

repo_path = "C:/Users/panne/logging-log4j2"
repo = git.Repo(repo_path)

git_commits = repo.iter_commits('--all')
commits = []
authors = []

for commit in git_commits:
    if commit.author.name not in authors:
        authors.append(commit.author.name)
        commits.append(commit)

for commit in commits:
    #print("Committed by %s on %s with sha %s" % (commit.committer.name, time.strftime("%a, %d %b %Y %H:%M", time.localtime(commit.committed_date)), commit.hexsha))
    repo.git.checkout(commit.hexsha)
    subprocess.call(['java', '-jar', 'ck.jar', repo_path, 'false', '0', 'true', "output/{}".format(commit.author.name)])

    