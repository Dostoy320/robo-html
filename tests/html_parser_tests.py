from nose.tools import *
import html_parser
import os
from html_parser.parsing import TextParsing
from html_parser.html_parser import build_HTML_from_TXT


def setup():
    testfile = open('html_parser/templates/test.txt', 'w')
    testfile.write('title: A Test Document')
    testfile.close()


def teardown():
    os.remove('html_parser/templates/test.txt')
    os.remove('html_parser/templates/test.html')


def test_get_file_name_from_path():
    textparsing = TextParsing()
    assert textparsing.get_file_name_from_path('/this/test/path.txt') == 'path'


def test_convert_txt_to_HTML():
    build_HTML_from_TXT('test')
    finishedFile = open('html_parser/templates/test.html', 'r')
    assert "<title>A Test Document</title>" in finishedFile.read()
