# Changelog

Record of changes, issues, etc.

## 02/16/2023

### Changes

Created passable endpoint generation - currently works as follows
* parses endpoint locations using regex, id's data models using gpt
* For each parsed endpoint + data model, generate docs

### Issues
* Docs are somewhat dreamed up - especially response bodies in endpoint docs
* GPT parsing response models is inefficient. Requires 3 passes of codebase instead of 2
  
### Todo
* Code cleanup - set up logging / proper debugging. Maybe switch to pycharm? This is a good stopping point
* Finetune generation model on real examples to prevent dreaming
* ID different candidate repos to test on