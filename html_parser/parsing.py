#!usr/bin/env python

from collections import defaultdict
from chardet.universaldetector import UniversalDetector
import re


class TextParsing():

    def get_file_name_from_path(self, path):
        d = defaultdict(int)
        for i in path:
            d[i] += 1

        split_path_group = path.split('/')
        return split_path_group[d['/']].split('.')[0]

    def detect_file_encoding(self, newfile):

        detector = UniversalDetector()

        for line in newfile:
            detector.feed(line)
            if detector.done:
                break

        detector.close()
        return detector.result['encoding']

    def convert_TXT_body_to_HTML(self, file_lines):

        timecode_pattern = "[0-9][0-9]:"

        description_pattern = "SD"

        on_screen_text_pattern = "OST"

        stripped_lines = []

        for line in file_lines:
            stripped_lines.append(line.strip('\n'))

        html_lines = []
        italics = False
        block = False
        voice = False

        for line in stripped_lines:
            timecode = False
            if not line.strip() and italics is True:
                html_lines.append('</i>')
                italics = False
            if not line.strip() and block is True:
                html_lines.append('</block>')
                block = False
            if not line.strip() and voice is True:
                voice = False
            if italics is True:
                html_lines.append(line)
            if block is True:
                html_lines.append(line)
            if voice is True:
                html_lines.append(line)
            if re.match(timecode_pattern, line):
                html_lines.append('<p>')
                timecode = True
            if re.match(description_pattern, line):
                html_lines.append('<i>')
                italics = True
            if re.match(on_screen_text_pattern, line):
                html_lines.append('<block>ON SCREEN TEXT<br>')
                block = True
            if html_lines[-1] == '<p>' and timecode is italics is False and block is False:
                voice = True
                html_lines.append(line)

        for line in html_lines:
            print line

        return html_lines
