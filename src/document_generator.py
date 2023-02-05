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

def generate_docs(code_index):

    # generate the intro for the endpoints.md file
    endpoint_header_prompt = f"""Write short intro for an endpoints.md file, supporting a cat facts api which provides daily cat facts"""
    endpoint_header_completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = endpoint_header_prompt,
                    temperature = 0,
                    max_tokens = 2048
        )

    intro_md = "# Endpoints \n" + endpoint_header_completion.choices[0].text

    template = {}

    # load the pre-defined doc template with {md:code} pairs 
    with open("generated_templates/cat_doc_template.json", "r") as file:
        template = json.load(file)

    with open("generated_docs/generated_docs.md","w") as md:
        md.write(intro_md)
        for endpoint in template["docs"]["endpoints"]:
            
            # create markdown using endpoint prompt + endpoint code file
            code_content = code_index[endpoint["code_name"]]
            generate_prompt = prompts.endpoint_prompt + code_content
            endpoint_completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt = generate_prompt,
                        temperature = 0,
                        max_tokens = 2048
            )
            md.write(endpoint_completion.choices[0].text)

    return
    
    






