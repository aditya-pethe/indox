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

def parse_summary():

    """
    opens the summary file and casts it to json, also cleans uneeded imports 
    """

    summary = {}
    with open("generated_summaries/summary.json", "r") as file:
        summary = json.load(file)

    for filepath in summary:
        path_data = summary[filepath]
        json_data = {}
        if type(path_data) == str:
            json_data = json.loads(path_data)
        else:
            json_data = path_data

        for imported_path in json_data["imports"]:
            if imported_path not in summary:
                json_data["imports"].remove(imported_path)

        summary[filepath] = json_data

    with open("generated_summaries/summary.json", "w") as file:
        json.dump(summary, file)
    
    return
# summary = {}
# n = 0

# with open("generated_summaries/summary.json","r") as file:
#     summary = json.load(file)
#     n = num_tokens(str(summary)) 
#     print(f"summary is {n} tokens")
