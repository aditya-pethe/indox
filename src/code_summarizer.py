from webbrowser import get
import requests
import base64
import urllib
import openai 
import pandas as pd
from urllib.parse import urlparse
import os
from dotenv import load_dotenv 
from utils import num_tokens, load_prompts
import json


from code_indexer import get_code_index
from utils import load_prompts

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()


def summarize_code_index(code_index):

    """
    Given a code_index, summarize the code_index and return:
    1. description of each file
    2. A list of imports for each file
    """
    cached_summary = {}
    with open("generated_summaries/summary.json","r") as file:
        cached_summary = json.load(file);

    # check if summary already exists for this codebase
    if cached_summary.keys() == code_index.keys():
        return

    summary_dict = {}

    for filepath,file_content in code_index.items():

        # TODO: average token length / file summary, but some files are more important than others - improve?
        tokens_per_summary = int((3000 - num_tokens(code_index.keys())) / len(code_index.keys()))

        summary_prompt = prompts["summary_prompt"] + f"""
        file name: {filepath} 
        file content: {file_content} 
        file_dir:{code_index.keys()}
        The "desc" field of the completion should be no longer than {tokens_per_summary} tokens"""

        summary_completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt = summary_prompt,
                        temperature = 0,
                        max_tokens = tokens_per_summary
            )
        
        summary_dict[filepath] = summary_completion.choices[0].text

    with open(f"generated_summaries/summary.json", "w") as file:
        # Encode the data as a JSON string and write it to the file
        json.dump(summary_dict, file)

    return

