from git import Repo
from pathlib import Path
from .content_extraction import extract_contents

def git_extraction(repo_url):
  # local_path = fr"./git_repos/{repo_url.split('/')[-1]}"
  repo_name = repo_url.rstrip("/").split('/')[-1]
  local_path = Path("git_repos")/repo_name
  
  local_path.parent.mkdir(parents=True, exist_ok=True)
  
  print("Repository name:", repo_name)
  print("Local path:", local_path)
  print("Parent path:", local_path.parent)
  
  # for root, dirs, files in os.walk(local_path):
  #   print("ROOT:", root)
  #   print("FILES:", files)
    
  if not local_path.exists():
    print("Repository not found locally. Cloning...")
    Repo.clone_from(str(repo_url),str(local_path))
    print(f'Repository Cloned at location: {local_path}')
  else:
    print("Repository already exists")
    
  print("\nRepository contents:")
  for item in local_path.iterdir():
    print(" -", item)
  
  return extract_contents(local_path, repo_name)
  
  
# git_extraction("https://github.com/Md-Danyal/student-management-system-flask")