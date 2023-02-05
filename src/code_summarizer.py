from webbrowser import get
import requests
import base64
import urllib
import openai 
import pandas as pd
from urllib.parse import urlparse
import os
from dotenv import load_dotenv 
from utils import num_tokens
import json


from code_indexer import get_code_index
from utils import load_prompts

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()


def summarize_code_index(code_index):

    MAX_SUMMARY_TOKENS = 4096 - num_tokens(code_index.keys)

    for filepath,file_content in code_index.items():

        file_tokens = 

        endpoint_completion = openai.Completion.create(
                        model="text-davinci-003",
                        prompt = prompts.summary_prompt,
                        temperature = 0,
                        max_tokens = 2048
            )
