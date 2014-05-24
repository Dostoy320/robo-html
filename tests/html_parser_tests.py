from nose.tools import *
import html_parser
from html_parser.parsing import TextParsing
from html_parser.html_parser import convertTxtToHTML


def setup():
    testfile = open('html_parser/templates/test.txt', 'w')
    testfile.close()


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"


def test_get_file_name_from_path():
    textparsing = TextParsing()
    assert textparsing.get_file_name_from_path('/this/test/path.txt') == 'path'


def test_convertTextToHTML():
    convertTxtToHTML('test')
