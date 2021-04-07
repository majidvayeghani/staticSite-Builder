from git import Repo

def autoPush(fileList,commit):
    repo_dir = '/home/majid/Desktop/project/'
    repo = Repo(repo_dir)
    file_list = fileList
    commit_message = "added" + commit
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    org = repo.remote('origin')
    org.push()