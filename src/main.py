from code_indexer import get_code_index
from code_summarizer import summarize_code_index
from template_generator import generate_template, rule_based_classification, embedding_classification
from document_generator import generate_intro_doc, generate_endpoint_docs, generate_model_docs
import os


def main():

    # gather code dictionary {filepath:filecontent} from a github repository
    # code_index = get_code_index()

    # classify the documents into a predefined template
    # generate_template(code_index, rule_based_classification)

    directory_name = 'generated_docs/complete_docs'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Document intro
    generate_intro_doc()

    # Document endpoints
    generate_endpoint_docs()

    # Document models
    generate_model_docs()

if __name__ == "__main__":
    main()