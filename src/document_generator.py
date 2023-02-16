# generate documentation given 1) the populated json template of documentation and 2) the code file index

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
from utils import load_prompts
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()

def write_endpoint_doc(endpoint):

    """
    Given an indexed endpoint file, write markdown documentation for it
    """

    code_index = {}
    with open("cache/code_cache.json","r") as file:
        code_index = json.load(file)["cached_index"]

    endpoint_filename = endpoint["code_name"]
    endpoint_code = code_index[endpoint_filename]
    endpoint_index = endpoint["endpoint_index"]
    
    ep_prompt = f"""
    Please write markdown documentation for the endpoint described in the following code. 
    You will be given the endpoint code, along with the data model used in the response. 
    
    Format output like so:

    ## Name of Endpoint

    ```
    GET /endpoint/path
    ```
    Description:

    Query Parameters: 

    Example Response:

    """

    endpoint_doc = ""

    for index in endpoint_index:

        start = index["line_indices"]["start_index"]
        end = index["line_indices"]["end_index"]

        code = "\n".join(endpoint_code.split("\n")[start:end])
        
        if index["response_model"] in code_index:
            model = code_index[index["response_model"]]
        else:
            model = "no model given"

        index_info = f"endpoint: {code} data model: {model}"

        generate_prompt = ep_prompt + index_info
        endpoint_completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = generate_prompt,
                    temperature = 0,
                    max_tokens = 1000
        )

        endpoint_doc += endpoint_completion.choices[0].text

    return endpoint_doc

def generate_docs():

    """
    Generate documentation for all endpoints in the code index
    """

    # # generate the intro for the endpoints.md file
    # endpoint_header_prompt = f"""Write short intro for an endpoints.md file, supporting a cat facts api which provides daily cat facts"""
    # endpoint_header_completion = openai.Completion.create(
    #                 model="text-davinci-003",
    #                 prompt = endpoint_header_prompt,
    #                 temperature = 0,
    #                 max_tokens = 2048
    #     )

    # intro_md = "# Endpoints \n" + endpoint_header_completion.choices[0].text

    template = {}
    endpoint_md_header = "#Endpoint Documentation \n"

    # load the pre-defined doc template with {md:code} pairs 
    with open("generated_templates/cat_doc_template.json", "r") as file:
        template = json.load(file)

    with open("generated_docs/generated_endpoint_docs.md","w") as md:
        md.write(endpoint_md_header)
        for endpoint in template["docs"]["endpoints"]:
            
            # create markdown using endpoint prompt + endpoint code file
            endpoint_doc = write_endpoint_doc(endpoint)
            md.write(endpoint_doc)

    return

template = {}
with open("generated_templates/cat_doc_template.json", "r") as file:
        template = json.load(file)

test_endpoint = template["docs"]["endpoints"][4]
    
endpoint_doc = write_endpoint_doc(test_endpoint)
with open("generated_docs/endpoint_docs.md","w") as md:
        md.write(endpoint_doc)





