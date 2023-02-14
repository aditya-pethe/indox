from code_indexer import get_code_index
from code_summarizer import summarize_code_index
from template_generator import generate_template, rule_based_classification, embedding_classification
from document_generator import generate_docs

# gather code dictionary {filepath:filecontent} from a github repository
code_index = get_code_index()

# summarize the code index
# summarize_code_index(code_index)

# generate an api doc template by populating the given template with filenames
generate_template(code_index, rule_based_classification)

# generate docs
# generate_docs(code_index)