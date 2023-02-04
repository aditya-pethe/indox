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
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

readme = ""

# with open("sample_repos/catfact_readme.md", "r") as file:
#         # Read the contents of the file and decode the JSON data
#         readme = file.read()

endpoint_header_prompt = f"""Using the given readme, please write the introduction to the endpoints.md file for documentation of this api
                        no need to go in depth on specific endpoints, simply list endpoints of interest to the user. readme.md: {readme}"""

endpoint_prompt = """Please write markdown docs for the endpoint described in the following code. Include:

                    1. Description of what the endpoint does
                    2. Example usage of the endpoint

                    Note that this markdown will be added to a larger endpoints.md file
                  """

endpoint_header_completion = openai.Completion.create(
                model="text-davinci-003",
                prompt = endpoint_header_prompt,
                temperature = 0,
                max_tokens = 4096
    )


