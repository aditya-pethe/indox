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
from document_generator import write_endpoint_doc
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
prompts = load_prompts()


def write_docs():
    
    summary = {}
    with open("generated_summaries/summary.json","r") as file:
        summary = json.load(file)

    filename = ""
    description = summary[filename]["description"]