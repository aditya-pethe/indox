# generate documentation given 1) the populated json template of documentation and 2) the code file index

from webbrowser import get
import openai 
import pandas as pd
from urllib.parse import urlparse
import os
from dotenv import load_dotenv 
from code_indexer import get_code_index
from utils import load_prompts
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()

def write_endpoint_doc(endpoint):

    """
    Given an indexed endpoint file, write markdown documentation for it
    """

    code_index = {}
    with open("cache/code_cache.json","r") as file:
        code_index = json.load(file)["cached_index"]
    
    # extract fields from endpoint object
    endpoint_filename = endpoint["code_name"]
    endpoint_code = code_index[endpoint_filename]
    endpoint_index = endpoint["endpoint_index"]
    
    ep_prompt = f"""
    Please write markdown documentation for the endpoint described in the following code. 
    You will be given the endpoint code, along with the data model used in the response. 
    
    Format output like so:

    ## Name of Endpoint

    ```
    GET /[insert path here]
    ```
    Description:

    Query Parameters: 
    - `param`: description

    Example Response:

    """

    endpoint_doc = ""

    for index in endpoint_index:

        # get file indices containing endpoint code, and read file
        start = index["line_indices"]["start_index"]
        end = index["line_indices"]["end_index"]

        code = "\n".join(endpoint_code.split("\n")[start:end])
        
        # handling for endpoint index info [code, data model] - only add data model if present in the codebase
        if index["response_model"] in code_index:
            model = code_index[index["response_model"]]
            index_info = f"endpoint: {code} data model: {model}"
        else:
            index_info = f"endpoint: {code}"

        # prompt to generate completion
        generate_prompt = ep_prompt + index_info
        endpoint_completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = generate_prompt,
                    temperature = 0,
                    max_tokens = 1000
        )

        endpoint_doc += endpoint_completion.choices[0].text

    return endpoint_doc

def write_model_doc(model):

    code_index = {}
    with open("cache/code_cache.json","r") as file:
        code_index = json.load(file)["cached_index"]

    model_code = code_index[model]
    model_prompt = f"""
    Please write markdown documentation for the data model used by an api described in the following code. 
    Given the data model object, please title the data model and write a short description of what it is.
    Afterwards, write a table containing each of the object keys, the data type of the key, and a description
    of what is.

## [Title] Model

Description:

| Key               | Type          | Description |
| ----------------- | ------------- | ----------- |
        
    {model_code}
    """
    generate_prompt = model_prompt
    model_completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = generate_prompt,
                    temperature = 0,
                    max_tokens = 1000
    )

    return model_completion.choices[0].text

def generate_endpoint_docs():

    """
    Generate endpoint documentation for all endpoints in the code index
    """

    template = {}
    endpoint_md_header = "# Endpoint Documentation \n"

    # load the pre-defined doc template with {md:code} pairs 
    with open("generated_templates/cat_doc_template.json", "r") as file:
        template = json.load(file)

    with open("generated_docs/complete_docs/endpoints.md","w") as md:
        md.write(endpoint_md_header)
        for endpoint in template["docs"]["endpoints"]:
            
            # create markdown using endpoint prompt + endpoint code file
            endpoint_doc = write_endpoint_doc(endpoint)
            md.write(endpoint_doc)

    return

def generate_model_docs():

    """
    Generate endpoint documentation for all models in the code index
    """

    template = {}
    endpoint_md_header = "# Model Documentation \n"

    # load the pre-defined doc template with {md:code} pairs 
    with open("generated_templates/cat_doc_template.json", "r") as file:
        template = json.load(file)

    with open("generated_docs/complete_docs/models.md","w") as md:
        md.write(endpoint_md_header)
        for model in template["docs"]["models"]:
            
            # create markdown using endpoint prompt + endpoint code file
            model_doc = write_model_doc(model["code_name"])
            md.write(model_doc)

    return

def generate_intro_doc():

    summary = {}
    with open("generated_summaries/summary.json","r") as file:
        summary = json.load(file)

    descriptions = {}
    for file in summary:
        descriptions[file] = summary[file]

    intro_prompt = f"""
    You are a documentation generator, tasked with generating the "intro.md" file for an API.
    You will be given a dictionary of filepath:file summary for files in the codebase.  Do not detail
    the specifics of the API, instead describe the primary functionality of the api, aimed at a developer
    who seeks to use this API. 

    Format your output in markdown

    summaries:
    {descriptions}
    """

    generate_prompt = intro_prompt
    intro_completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = generate_prompt,
                    temperature = 0,
                    max_tokens = 1000
    )

    intro_md = intro_completion.choices[0].text
    with open("generated_docs/complete_docs/intro.md","w") as md:
        md.write(intro_md)
    # return intro_md
    

# template = {}
# with open("generated_templates/cat_doc_template.json", "r") as file:
#         template = json.load(file)

# test_model = template["docs"]["models"][1]["code_name"]
    
# model_doc = write_model_doc(test_model)
# intro_md = generate_overview_doc()
# with open("generated_docs/intro.md","w") as md:
#         md.write(intro_md)





