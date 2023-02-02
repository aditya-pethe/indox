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

* Input: Repository directory path
* Output: Text representation of code structure.

Early Files & Modules 

* **code_index.py** - given dir path, return the following:
  * A file subtree of the git repo under that directory
  * A dictionary of {filename:filecontent} of all code files under the tree

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
