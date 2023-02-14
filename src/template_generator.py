# Module for classfying code files into template structure . The idea 
# is to prep for document generation by populating the template with
# the file names, so generation prompts can be as specific as possible.

from importlib.resources import read_binary
from webbrowser import get
import requests
import base64
import urllib
import openai 
import pandas as pd
from urllib.parse import urlparse
import os
from dotenv import load_dotenv 
from code_indexer import get_code_index
from utils import load_prompts, num_tokens


import json

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()


def write_template(write_obj, doc_template_path = "doc_templates/api_template.json", name = "cat_doc_template"):

    """
    Given a write_obj with models and endpoints, this function will write the template to a json file
    """

    with open(doc_template_path, "r") as file:
        template = json.load(file)
    
    template["docs"]["models"] = write_obj["models"]

    # begin endpoint indexing
    for endpoint in write_obj["endpoints"]:
        filename = endpoint["codename"]
        endpoint_index = 

    template["docs"]["endpoints"] = write_obj["endpoints"]

    with open(f"generated_templates/{name}.json", "w") as file:
        json.dump(template, file)

    return 

def rule_based_classification(code_index):

    """
    A simple rule-based classification function that uses filenames to classify the code
    """

    write_object = {
            "models":[],
            "endpoints":[]
        }

    for filepath in code_index:

        path_list = filepath.split("/")

        if "route" in filepath or "endpoint" in filepath:
            write_object["endpoints"].append({
                "markdown_name" : f"{path_list[-1]}.md",
                "code_name": f"{filepath}"
            })

        elif "model" in filepath:
            write_object["models"].append({
                "markdown_name" : f"{path_list[-1]}.md",
                "code_name": f"{filepath}"
            })

    return write_object

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

def endpoint_indexer(code_name):
    """
    This attempts to create a template for all endpoints in a file, and relevant imports
    """

    code_index = {}
    summary = {}

    with open("generated_summaries/summary.json","r") as file:
        summary = json.load(file)
    with open("cache/code_cache.json","r") as file:
        code_index = json.load(file)

    # get the file contents + imports for the given code file
    code_imports = summary[code_name]["imports"]
    import_desc = dict((path, summary[path]["description"]) for path in code_imports)
    code_content = code_index["cached_index"][code_name]


    endpoint_indexer_prompt = prompts["endpoint_indexer_prompt"]

    complete_prompt = f"""
    {endpoint_indexer_prompt} 
    code content: {code_content}
    """ 

    capped_max = 4096 - num_tokens(complete_prompt)

    endpoint_indexer_completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt = complete_prompt,
                        temperature = 0,
                        max_tokens = capped_max
            ).choices[0].text

    obj = json.loads(endpoint_indexer_completion)

    with open("generated_templates/endpoint_template.json","w") as file:
        json.dump(obj, file)

    return


def prompt_classfication():

    """
    input: template generation prompt + api doc template + file summary dict
    output: a populated template, with file names in approriate positions in doc structure
    """

    template_generation_prompt = prompts["template_generation_prompt"]
    summary = ""
    doc_template = ""
    with open("generated_summaries/summary.json","r") as file:
        summary = str(json.load(file))

    with open("doc_templates/api_template.json","r") as file:
        doc_template = str(json.load(file))

    complete_prompt = f"""
    {template_generation_prompt} 
    summary dictionary: {summary}
    doc template: {doc_template}
    """ 

    capped_max = 4096 - num_tokens(complete_prompt)

    template_completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt = complete_prompt,
                        temperature = 0,
                        max_tokens = capped_max
            ).choices[0].text

    with open("generated_templates/cat_doc_template.json","w") as file:
        json.dump(template_completion, file)

    return

def embedding_classification(code_data, target_folders):
    return

def generate_template(code_index, classification):
    write_object = classification(code_index)
    write_template(write_object)
    return

# prompt_classfication()
# filename = "app/routes/fact.routes.js"
# endpoint_indexer(filename)