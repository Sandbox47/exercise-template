# Tutorium
This directory is a template for a tutorium directory

## How to use
You can use the python script `CreateNewSheet.py` to automatically perform a `git pull` to update the repo and create a new sheet directory. 

### Naming 
You can change the naming standard within the script by changing the prefix and the suffix. 
Then the every time you run the script you will create a new directory named `{sheetDirPrefix}{sheetNumber}` (ex.: Sheet1) that contains `{pdfNamePrefix}{sheetNumber}{pdfNameSuffix}.tex` file (ex.: Sheet1_AliceBob) and a figures folder.

### Latex Headers
You can change the latex headers in `LatexTemplate/styles/FormatAndHeader.tex`
