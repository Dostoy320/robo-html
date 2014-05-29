#!/usr/bin/env python
"""Converst txt file into html based on a template"""

from jinja2 import Template
import os
from parsing import TextParsing

dir = os.path.dirname(__file__)


def set_template_variables(file_lines):

    if "title:" in file_lines[0]:
        title = file_lines[0].split(': ')[1].strip('\n')
    else:
        title = "Generic Title"

    return title


def build_HTML_from_TXT(filename):

    textparsing = TextParsing()

    # Get a copy of the template to use for new .html file creation
    f = open(os.path.join(dir, 'templates/basic.html'), 'r+')
    template = Template(f.read())
    f.close()

    newfile = open(os.path.join(dir, 'templates/%s.txt') % filename, 'r+')

    file_lines = newfile.readlines()

    # if textparsing.detect_file_encoding(newfile) == 'UTF-16LE':
    #     file_lines = [line.decode("utf-16", "ignore") for line in newfile]
    # else:
    #     file_lines = newfile.readlines()

    newfile.close()

    title = set_template_variables(file_lines)

    html_lines = textparsing.convert_TXT_body_to_HTML(file_lines)

    savefile = open(os.path.join(dir, 'templates/%s.html') % filename, 'w')
    savefile.write(template.render(title=title, lines=html_lines))

    savefile.close()
