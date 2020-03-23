import git
from threading import Timer
repo = git.Repo('LOCATION OF REPO e.g C:/GITHUBREPO')
def pull():
    repo.remotes.origin.pull()
    current = repo.head.commit
    repo.remotes.origin.pull()
    Timer(20700, pull).start()
        
   
pull()
    
