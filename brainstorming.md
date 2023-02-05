# Brainstorming

## Product Description

Generate markdown docs from code

Indox is a tool that allows developers to automatically generate documentation from their code. Instead of traditional templated document generation, Indox will leverage Large Language Models to dynamically create useful documentation, requiring little to no effort from developers.

The end product can take a few different forms:
* github app - first class actor in github with access to org repositories
* Oauth app - a more limited scope app which can request access to a repostory
* package - an open source package or cli-tool which just needs to be installed
#
## User Workflow

Ideally, a developer should be able to use Indox by doing the following:

1. Grant Indox permissions / handle authentication to allow read/write access to repository
2. Specify the directory path that serves as a "root", where documentation will begin
3. Receive a generated docs/ directory, containing markdown files with complete documentation
#
## User Requirements

A completed project should meet the following requirements:

* No code / user input beyond filepath
* Github Integration / permissions 
* High document quality - documentation should be complete / human usable after autogeneration
* automatically updating - code changes etc. should be reflected in the docs
  
#
## Software Components

### Github Integration

#
### Code Indexing

This component will read repository code under the specified directory, and represent it to the LLM in a meaningful way.

* **Input**: Repository directory path
* **Output**: Text representation of code structure.


Early Files & Modules 

* **code_index.py** - given dir path, return the following:
  * A file subtree of the git repo under that directory
  * A dictionary of {filename:filecontent} of all code files under the tree

#
### Code Summarizer

Their needs to be a high level representation of the codebase that the LLM can understand in a single read, < 2048 tokens. This will be used for  code classification + template generation.

It will also be used to represent the dependency tree of the repo

* **Input**: 
  * code_index, dict of {filename:filecontent}
  * predefined documentation template / file structure:
* **Output**: Populated documentation template with {md:code} mapping

Steps:

1. For each code file, generate a condensed summary, such that the dict {filename:summary} is within the prompt limit
2. For each summary, ask for a list of imports which are also in the file tree
3. Return both a) a dict of file summaries and b) a dependency tree

#
### Template Generation

There is a token limit of 2048 tokens per api call, so this component will break up the codebase into chunks and arrange them into a template that can be passed to the doc generator

* **Input**: 
  * Summarization dict {filepath|filecontent} (from file summarizer) 
  * predefined documentation template / file structure:
* **Output**: Populated documentation template with {md:code} mapping

This component is nuanced and difficult. It is made complicated by the fact that a single .md doc might require multiple code files to be generated. For example, an endpoint.md file requires the endpoint definition + model req/res definition. Thus, we need a file dependency tree - i.e imports - to be stored

Steps:

1. For each code file, generate a condensed summary, such that the dict {filename:summary} is within the prompt limit
2. Using this dictionary, in addition to an intent generated from the readme, create a candidate set of essential code files for creating the docs. This can be done 2 ways:
   1. Produce a dict {md filename: list of code filenames}
   2. Produce a list of code filenames, and attempt to generate a single md doc in one shot. This is simpler, but may run into prompt constraints
3. Pass the pruned candidate set to the document generator


#
### Document Generator
  
  This component will generate documentation given the file subtree and code content. Another input to be added later could be custom user prompts.

  * Input: File Subtree + Code dictionary
  * Output: Document Tree + Markdown Document Dictionary

Early Files & Modules 

  * **base_prompt.txt** - Handwritten prompt determining how 
  * **output_format.txt** - Prompt specifying how LLM should format output 
  * **document_generator.py** - given file tree + code dict, generate the following
    * file tree of markdown documentation
    * dictionary of {filename:filecontent}, where the files are markdown docs

#
### File Writing

This component will write files to the repository, given the textual representation from the Document Generator

Early Files & Modules
* **output_parser.py** - given LLM output, parse this into writeable content
  * parse doc file tree
  * Populate with markdown content
* **file_writer.py** - write output to github repository under docs/ dir
