import os
from git import Repo
from os.path import join, getsize

# Set environment variables
#os.environ['REPO_PATH'] = '/home/rodrigo/codigo/codigos_pruebas/test_repo'



COMMITS_TO_PRINT = 3

def print_commit_data(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))
    
def print_repository_info(repo):
    print('Repository description: {}'.format(repo.description))
    print('Repository active branch is {}'.format(repo.active_branch))
    for branch in repo.branches:
        print('Branch named "{}" '.format(branch))

    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))
    status = repo.git.status()
    print("Status", status)

def print_diff(repo):
    hcommit = repo.head.commit
    hcommit.diff()                  # diff tree against index
    hcommit.diff('HEAD~1')          # diff tree against previous tree
    hcommit.diff(None)              # diff tree against working tree

    index = repo.index
    index.diff()                    # diff index against itself yielding empty diff
    index.diff(None)                # diff index against working copy
    index.diff('HEAD')              # diff index against current HEAD tree


repo_path = '/home/rodrigo/codigo/codigos_pruebas/test_repo'
# Repo object used to interact with Git repositories


# check that the repository loaded correctly
def check_directory(repo_path):
    repo = Repo(repo_path)
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository_info(repo)

        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('{}'.format(repo.active_branch)))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit_data(commit)
            pass

    else:
        print('Could not load repository at {} :'.format(repo_path)) 

check_directory(repo_path)




def check_gits_directories(directory):
    directories_with_git = []
    standard_non_util_dirs= ['lib' , '.vscode' , 'bin','share','.git','etc' ,'include' ]
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            directories_with_git.append(root)
       
        for x in  standard_non_util_dirs:   
            if x in dirs:
                dirs.remove(x)
    
    return directories_with_git        


def repository_uptodate(repo):
    status = repo.git.status()
    uptodate= False 
    if "Your branch is up to date with" in status:
        print("Up to date")
        uptodate = True
    return uptodate        



standard_non_util_dirs= ['lib' , '.vscode' , 'bin','share','.git','etc' ,'include' ]
