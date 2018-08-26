# HomeworkGenerator

### A framework/tool for quickly generating Maths homework question and answer sheets as .pdf files (aimed ages ~6-14).

---

#### Software Licence: This software is available under GPL, which allows free usage and modification - with the restriction that derivative work must be available under the same licence. If you want to adapt this for use as/in a commercial product, contact me to discuss a commercial licence

This software is (at least initially) being developed with a focus on producing homeworks corresponding to the 
syllabuses for the first 3 years of secondary school mathematics in the UK. Pull requests for functionality 
for other subjects / knowledge levels will be appreciated and reviewed, but I won't actively work on them myself.
(reasoning for this is that those are the ages my mother teaches, this is primarily for her use)

## Setup Requirements:

> Python 3.x

> Numpy

> Gooey [available via pip, link to github repo](https://github.com/chriskiehl/Gooey)

> md2py (available via pip install markdown2py)
> Note: markdown2py is built in python2, I ported my version to python3 to work with this setup, 
> but I am trying to find an alternative that works as well as md2py. 
> This is only used at the last step, to convert the .md files to .pdf files

---

## Usage:

> Run 'python homework_generator.py'

> In the GUI, enter a title, choose a topic, and enter the number of questions required

> Use 'make_pdfs' script, or md2py directly (usage 'md2py --theme=github <file.md>'), or an alternative, to make .pdfs from the .md files

