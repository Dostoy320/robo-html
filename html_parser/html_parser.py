#!/usr/bin/env python
"""Converst txt file into html based on a template"""

from jinja2 import Template


def convertTxtToHTML(filename):

    # Get a copy of the template to use for new .html file creation
    f = open('templates/basic.html', 'r+')
    template = Template(f.read())
    f.close()

    newfile = open('templates/%s.txt' % filename, 'r+')

    for line in newfile:
        if "title:" in line:
            title = line.split(':')[1].strip('\n')
        if not line.strip():
            return

    newfile.close()

    savefile = open('templates/%s.html' % filename, 'w')
    savefile.write(template.render(title=title))

    savefile.close()
