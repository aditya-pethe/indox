import requests
import base64
import urllib
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

MY_AUTH = (os.getenv("GITHUB_USER"), os.getenv("GITHUB_PAT"))

def parse_url(repo_url):
    parts = urlparse(repo_url).path.split("/")
    owner = parts[1]
    repo = parts[2]
    dir = parts[-1] + "/"
    return owner, repo, dir

def get_tree(owner, repo, dir, branch='master'):
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1', auth=MY_AUTH)
    if response.status_code == 200:
        repo_tree = response.json()
        return [item for item in repo_tree['tree'] if item['path'].startswith(dir) and item['type'] == 'blob']
    else:
        return []

def get_content(owner, repo, file_sha):
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/git/blobs/{file_sha}', auth=MY_AUTH)
    if response.status_code == 200:
        file_content = response.json()
        return file_content["content"]
    else:
        return ''

def get_app_files(owner, repo, dir, branch='master'):
    app_files = {}
    app_tree = get_tree(owner, repo, dir, branch)
    for item in app_tree:
        file_content = get_content(owner, repo, item['sha'])
        app_files[item['path']] = file_content
    return app_files

def get_code_index(dir_url = "https://github.com/alexwohlbruck/cat-facts/tree/master/app"):
    owner,repo,dir = parse_url(dir_url)
    tree = get_tree(owner, repo, dir)
    app_files = get_app_files(owner, repo, dir)
    return app_files

# res = get_code_index()
# print(res.keys())