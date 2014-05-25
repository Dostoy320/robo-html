from nose.tools import *
import html_parser
import os
from html_parser.parsing import TextParsing
from html_parser.html_parser import convert_txt_to_HTML


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
    convert_txt_to_HTML('test')
    finishedFile = open('html_parser/templates/test.html', 'r')
    assert "<title>A Test Document</title>" in finishedFile.read()
