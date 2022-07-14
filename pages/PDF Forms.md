Title: PDF Forms
Author: Philip
Date: 2021-06-08
Category: Miscellaneous
status:draft

__ToDo__
- [ ] Get these to run as apps on Server
- [ ] Extra - Create a Python GUI that can be run locally?

PDF Form Filling
================

Aim: enable the user to generate a set of PDFs - each filled with a record of input data.

Method: create two macros/apps. The first to get list of form-field names and the second to generate PDFs with imputed data.

## 1. PDF Form Reader
Aim: get the form-field names from a PDF document.  

Inputs
- PDF document

Outputs
- List of form-fields names
- PDF document with each form-field filled with their own form-field name

## 2. PDF Form Filler
Aim: generate a set of PDFs - one for each record of input data. The number of generated PDFs will equal the number of records in the data.

This app/macro requires that the data column names be mapped to the PDF form-field names.

Inputs
- PDF Document
- Data
- Mapping (Data column names $\leftrightarrow$ PDF form-field names)

Outputs
- Filled PDFs

a## Process
Assume the user starts with a _PDF form_ and _input data_ to impute.

The steps are as follows,
1. **Run the _PDF Form Reader_**
Select PDF Document from which to extract a list of form-field names
2. **Create mapping file**
Manually map the form-field names to the data column names
3. **Run the _PDF Form Filler_**
Select PDF Document, data to impute and newly created mapping file. Select destination to save PDFs

*If the mapping file exists then skip steps 1 and 2.



## Questions
- [ ] Can I run the Python Tool on Server?
- [ ] Can I install and run a Python package on Server?
- [ ] Can I upload file (and use file browser) on Server?
- [ ] Can I write to Box (or say Dropbox) from Server?
- [ ] Can you generate multiple PDFs locally to download from Gallery?

