from git import Repo
from pathlib import Path
from .content_extraction import extract_contents

def git_extraction(repo_url):
  # local_path = fr"./git_repos/{repo_url.split('/')[-1]}"
  repo_name = repo_url.split('/')[-1]
  local_path = Path("git_repos")/repo_name
  
  local_path.parent.mkdir(parents=True, exist_ok=True)
  
  if not local_path.exists():
    repo = Repo.clone_from(repo_url,local_path)
    print(f'Repository Cloned at location: {local_path}')
  else:
    print("Repository already exists")
  
  return extract_contents(local_path, repo_name)
  
  
# git_extraction("https://github.com/Md-Danyal/student-management-system-flask")