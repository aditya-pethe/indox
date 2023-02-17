import re

# define the regex pattern
endpoint_patterns = {
    "express_router":re.compile(r"router\.(get|post|put|delete)\('(.+?)',.*\)", re.DOTALL)
}

import_patterns = {
    "js_require":re.compile(r"const\s+(\w+)\s*\.require\s*\(\s*[\"']\s*\.\/.*?/(\w+)\s*[\"']\s*\)")
}

def get_import_headers(file):

    """
    Matches all "require" or "import" lines and returns as an import header to be used in prompt
    """

    import_headers = []
    
    for line in file.split('\n'):
        if "require(" in line or " import " in line:
            import_headers.append(line)
    return '\n'.join(import_headers)

def match_endpoint(file, pattern=endpoint_patterns["express_router"]):

    """
    uses a given regex pattern to match every api endpoint and file line indices of start/end of ep
    """

    endpoint_list = []
    match = False
    start_idx = None
    end_idx = None
    paren_stack = []
    paren_map = {
        ")":"("
    }
    
    for line_number, line in enumerate(file.split('\n')):
        # search for the pattern in the line
        if not match:
            match = pattern.search(line)
        # if a match is found, print the line number and the matched text
        if match:
            if start_idx == None:
                start_idx = line_number
                # print(f"Match found on line {start_idx}: {match.group()}")
            else:
                for char in line:
                    if char == "(":
                        paren_stack.append(char)
                    elif char == ")":
                        if len(paren_stack)==0:
                            end_idx = line_number
                            endpoint_list.append((start_idx, end_idx))
                            # response_code = file.split("\n")[start_idx+1:end_idx]
                            # for model_name, filepath in model_dict.items():
                            #     if model_name in " ".join(response_code):
                            #         print(f"Endpoint from {start_idx} to {end_idx} uses {model_name} model")
                            # print(f"endpoint form {start_idx,end_idx}")
                            match = False
                            start_idx = None
                        else:
                            paren_stack.pop(-1)
    return endpoint_list
