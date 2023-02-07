import os
import json
from nltk.tokenize import word_tokenize
import tiktoken

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

    def num_tokens_from_string(string, encoding_name = "gpt2"):

        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    res = 0
    if type(data) != str:
        res = num_tokens_from_string("".join(data))
    else:
        res = num_tokens_from_string(data)
    return res

summary = {}
n = 0

with open("generated_summaries/summary.json","r") as file:
    summary = json.load(file)
    n = num_tokens(str(summary)) 
    print(f"summary is {n} tokens")
