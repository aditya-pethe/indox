# Module for reading a github repository and returning a dict {filepath, filecontent}

import requests
import base64
import urllib
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

MY_AUTH = (os.getenv("GITHUB_USER"), os.getenv("GITHUB_PAT"))

def parse_url(repo_url, paths = ["app/models","app/routes"]):

    """
    give a repo url, and list of file paths
    """
    
    parts = urlparse(repo_url).path.split("/")
    owner = parts[1]
    repo = parts[2]
    if paths == None:
        paths = [parts[-1]]

    return owner, repo, paths

def get_tree(owner, repo, paths, branch='master'):
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1', auth=MY_AUTH)
    if response.status_code == 200:
        repo_tree = response.json()

        pruned_tree = []

        for item in repo_tree['tree']:
            for path in paths:
                if item["path"].startswith(path):
                    if item["type"] == "blob":
                        pruned_tree.append(item)

        return pruned_tree
    else:
        return []

def get_content(owner, repo, file_sha):
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/git/blobs/{file_sha}', auth=MY_AUTH)
    if response.status_code == 200:
        file_content = response.json()
        return base64.b64decode(file_content["content"]).decode('utf-8')
    else:
        return ''

def get_app_files(owner, repo, paths, branch='master'):
    app_files = {}
    app_tree = get_tree(owner, repo, paths, branch)
    for item in app_tree:
        file_content = get_content(owner, repo, item['sha'])
        app_files[item['path']] = file_content
    return app_files

def get_code_index(dir_url = "https://github.com/alexwohlbruck/cat-facts/tree/master/app"):
    owner,repo,paths = parse_url(dir_url)
    tree = get_tree(owner, repo, paths)
    app_files = get_app_files(owner, repo, paths)
    return app_files

# res = get_code_index()
# print(res.keys())