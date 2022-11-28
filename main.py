import git_ck
import os

folder = "To_Analyze"

def check():
    if os.path.exists(folder):
        content = os.listdir(folder)
        if content is not None:
            return 0
    else:
        git_ck.clone_repo()

if __name__ == '__main__':
    try:
        check()
    except:
        print("Warning")
    repo = git_ck.repo_to_use()
    git_commits = git_ck.get_commits(repo)
    git_ck.year_ck_metrics(git_commits)