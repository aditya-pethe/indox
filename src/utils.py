import os
from nltk.tokenize import word_tokenize

def load_prompts():

    prompts = {}

    for filename in os.listdir("prompts"):
        fpath = os.path.join("prompts", filename)
        with open(fpath) as f:
            fcontent = f.read()
            file_key = filename.replace(".txt","")
            prompts[file_key] = fcontent

    return prompts

def num_tokens(data):
    res = 0
    if type(data) != str:
        res = word_tokenize("".join(data))
    else:
        res = word_tokenize(data)
    return res
