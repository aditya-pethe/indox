# Module for classfying code files into template structure using open ai api

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
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def write_template(write_obj, doc_template_path = "doc_templates/api_template.json", name = "cat_doc_template"):

    # Open the file for reading
    with open(doc_template_path, "r") as file:
        # Read the contents of the file and decode the JSON data
        template = json.load(file)

    # Make the desired modifications to the data
    
    template["docs"]["models"] = write_obj["models"]
    template["docs"]["endpoints"] = write_obj["endpoints"]

    # Open the file for writing
    with open(f"generated_templates/{name}.json", "w") as file:
        # Encode the data as a JSON string and write it to the file
        json.dump(template, file)

    return 

def rule_based_classification(code_index):

    write_object = {
            "models":[],
            "endpoints":[]
        }

    for filepath in code_index:

        path_list = filepath.split("/")

        if "route" in filepath or "endpoint" in filepath:
            write_object["endpoints"].append({
                f"{path_list[-1]}.md": {
                "code_files":f"{filepath}"
                }
            })

        elif "model" in filepath:
            write_object["models"].append({
                f"{path_list[-1]}.md": {
                "code_files": f"{filepath}"
                }
            })

    return write_object

def create_embeddings(code_index):

    code_df = pd.DataFrame({
        "file_path":code_index.keys(),
        "file_content":code_index.values()
    })

    return

def embedding_classification(code_data, target_folders):
    return

def generate_template(code_index, classification):
    write_object = classification(code_index)
    write_template(write_object)
    return

