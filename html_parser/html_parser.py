#!/usr/bin/env python
"""Converst txt file into html based on a template"""

from jinja2 import Template
import os

dir = os.path.dirname(__file__)


def setTemplateVariables(newfile):

    with newfile as f:
        first_line = f.readline()

    if "title:" in first_line:
        title = first_line.split(': ')[1].strip('\n')
    else:
        title = "Generic Title"

    return title


def convertTxtToHTML(filename):

    # Get a copy of the template to use for new .html file creation
    f = open(os.path.join(dir, 'templates/basic.html'), 'r+')
    template = Template(f.read())
    f.close()

    newfile = open(os.path.join(dir, 'templates/%s.txt') % filename, 'r+')

    title = setTemplateVariables(newfile)

    newfile.close()

    savefile = open(os.path.join(dir, 'templates/%s.html') % filename, 'w')
    savefile.write(template.render(title=title))

    savefile.close()
