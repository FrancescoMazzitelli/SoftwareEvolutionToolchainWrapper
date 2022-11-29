import git_ck
import os
import analysis

folder = "To_Analyze"

def check():
    if os.path.exists(folder):
        content = os.listdir(folder)
        if content is not None:
            return 0
    else:
        git_ck.clone_repo()

if __name__ == '__main__':
    #git_ck.config_git_bash()

    if not os.path.exists("output"):
        path = os.path.join("output")
        os.mkdir(path)
    try:
        check()
    except:
        print("Warning")

    #git_ck.checkout_repo()
    repo = git_ck.repo_to_use()
    git_ck.print_current_branch(repo=repo)
    git_commits = git_ck.get_commits(repo)
    git_ck.year_ck_metrics(git_commits)
    
    git_ck.delete_unnecessary(file_to_keep="class")

    analysis.metrics_average()
