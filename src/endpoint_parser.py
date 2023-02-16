import re

# define the regex pattern
endpoint_patterns = {
    "express_router":re.compile(r"router\.(get|post|put|delete)\('(.+?)',.*\)", re.DOTALL)
}

import_patterns = {
    "js_require":re.compile(r"const\s+(\w+)\s*\.require\s*\(\s*[\"']\s*\.\/.*?/(\w+)\s*[\"']\s*\)")
}

def get_import_headers(file):
    import_headers = []

    
    for line in file.split('\n'):
        if "require(" in line or " import " in line:
            import_headers.append(line)
    return '\n'.join(import_headers)

# Example usage
file_path = 'example.js'
import_headers = get_import_headers(file_path)
print(import_headers)

# import_pattern = fr"const\s+.*?\s*=\s*require\s*\(\s*[\"']\s*\.\/.*?/({endpoint[0]})\s*[\"']\s*\)"
def extract_models(file):
    model_dict = {}
    pattern = re.compile(r'require\([\'"](.+?)[\'"]\)')

    for line in file.split('\n'):
        match = pattern.search(line)
        if match:
            filepath = match.group(1)
            model_name = re.search(r'([^/]+)$', filepath).group(1)
            model_dict[model_name] = filepath

    return model_dict
# # pattern = re.compile(r"router\.(get|post|put|delete)\('(.+?)',.*\)", re.DOTALL)
def match_imports(file, pattern):
    import_dict = {}
    for line_number, line in enumerate(file.split('\n')):
        match = pattern.search(line)
        if match:
            import_name = match.group(1)
            import_path = match.group(2)
            import_dict[import_name] = import_path
    return import_dict

def match_endpoint(file, pattern=endpoint_patterns["express_router"]):

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
                            print(f"endpoint form {start_idx,end_idx}")
                            match = False
                            start_idx = None
                        else:
                            paren_stack.pop(-1)
    return endpoint_list

def match_models_in_response(file, endpoint_list, required_models):
    # function to match models in endpoint responses
    for start_idx, end_idx in endpoint_list:
        response_lines = file.split('\n')[start_idx+1:end_idx]
        for line in response_lines:
            for model, filepath in required_models.items():
                # search for the variable name in the response using regex
                var_match = re.search(f"\b{model}\b", line)
                if var_match:
                    # print the model name and filepath if it is used in the response
                    print(f"{model} used in response with filepath {filepath}")
                    
# fact_endpoint = ""
# with open("sample_repos/facts.js","r") as file:
#     fact_endpoint = file.read()

# print(get_import_headers(fact_endpoint))
# endpoints = re.findall(endpoint_patterns["express_router"],fact_endpoint)

# for endpoint in endpoints:
#     print(endpoint)
# endpoint_list = match_endpoint(fact_endpoint, endpoint_patterns["express_router"])
# model_dict = extract_models(fact_endpoint)
# print(model_dict)
# match_models_in_response(fact_endpoint, endpoint_list, model_dict)

# print(match_imports(fact_endpoint, import_patterns["js_require"]))
# print(extract_models(fact_endpoint))