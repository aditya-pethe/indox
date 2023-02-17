# Module for classfying code files into template structure . The idea 
# is to prep for document generation by populating the template with
# the file names, so generation prompts can be as specific as possible.

from importlib.resources import read_binary
from webbrowser import get
import openai 
import pandas as pd
from urllib.parse import urlparse
import os
from dotenv import load_dotenv 
from code_indexer import get_code_index
from utils import load_prompts, num_tokens
from endpoint_parser import match_endpoint, get_import_headers
import json
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()


def write_template(write_obj, doc_template_path = "doc_templates/api_template.json", name = "cat_doc_template"):

    """
    Given a write_obj with models and endpoints, this function will
    fill out the generated template file, and be ready for generation
    """

    with open(doc_template_path, "r") as file:
        template = json.load(file)
    
    template["docs"]["models"] = write_obj["models"]

    # index each endpoint, given the file name
    for i,endpoint in enumerate(write_obj["endpoints"]):
        filename = endpoint["code_name"]
        endpoint_index = endpoint_indexer(filename)
        write_obj["endpoints"][i]["endpoint_index"] = endpoint_index

    template["docs"]["endpoints"] = write_obj["endpoints"]

    with open(f"generated_templates/{name}.json", "w") as file:
        json.dump(template, file)

    return 

def endpoint_indexer(filename):
    """
    This will add important data to the generated template that allows endpoint documentation
    
    "line_indices": {"start_index": start, "end_index": end}, // where the code is in the file
    "response_model": data_model_completion // the filepath of the data model

    """
    code_index = get_code_index()
    # Now we are going to produce our documentation template:
    code = code_index[filename]

    endpoint_indices = match_endpoint(code)
    endpoint_imports = get_import_headers(code)

    summary = {}
    possible_answers = ""
    with open("generated_summaries/summary.json","r") as file:

        summary = json.load(file)
        possible_answers = summary[filename]["imports"]
    
    prompt_header = """use the provided api endpoint and import 
    statements to give the filepath for the data model that the endpoint
    uses in its response, and return only the filepath as a string. Do not include 
    any other text in your output. Your final output should be a single line 
    with the filepath as the only content. This filepath should be selected
    from one of the filepaths in the "possible answers" list. The output should contain
    no newline characters
    """

    with open("generated_templates/endpoint_template.json","w") as file:
        write_obj = []
        for ep in endpoint_indices:

            start,end = ep
            code = "\n".join(code.split("\n")[start:end])
            data_model_prompt = prompt_header + f"""
            code: {code} 
            file header: {endpoint_imports}
            possible answers: {possible_answers}"""

            data_model_completion = openai.Completion.create(
                            model="text-davinci-003",
                            prompt = data_model_prompt,
                            temperature = 0,
                            max_tokens = 12
                ).choices[0].text

            # clean up model output 
            data_model_completion = data_model_completion.replace("\n","")
            data_model_completion = data_model_completion.replace("'","")

            ep_obj = {
                "line_indices": {"start_index": start, "end_index": end}, 
                "response_model": data_model_completion
            }
            write_obj.append(ep_obj)
        
        # ep_template = {"ep_index":write_obj}
        # file.write(json.dumps(ep_template))

    # obj = json.loads(endpoint_indexer_completion

    return write_obj

def prompt_classfication():

    """
    Given the summary dictionary, this attempts to classify all the files into 
    the generation template using the completion endpoint
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

def rule_based_classification(code_index):

    """
    A simple rule-based classification that classifies files into
    endpoints or models, using keyword / name matching
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

def embedding_classification(code_data, target_folders):
    return

def generate_template(code_index, classification):

    """
    Given a function to classify the files into categories [endpoint/model]
    generate the documentation template
    """

    write_object = classification(code_index)
    write_template(write_object)
    return

# prompt_classfication()
# filename = "app/routes/fact.routes.js"
# endpoint_indexer(filename)