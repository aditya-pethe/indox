from code_indexer import get_code_index
from code_summarizer import summarize_code_index
from template_generator import generate_template, rule_based_classification, embedding_classification
from document_generator import generate_docs
from endpoint_parser import match_endpoint, import_headers

# gather code dictionary {filepath:filecontent} from a github repository
# code_index = get_code_index()

# classify the documents into a predefined template
# generate_template(code_index, rule_based_classification)

# Now we are going to produce our documentation template:
generate_docs()
