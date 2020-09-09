from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from .formatconverter import FormatConverter

def json(request):
    # DONE fetch from command line
    # DONE split at every '\n\n' , or see if we can collapse/massage the data in some cleaner way
    # DONE use json.dumps to turn most of the content into compliant JSON
    # DONE refactor to separate classes as needed
    # TODO figure out how Pythons 'unittest' works and implement
    # TODO test to destruction as needed
    # TODO polish code
    # TODO REMOVE THE DEBUG FLAG!!!!

    converter = FormatConverter()

    # get the text from a dump of status
    txt = Path('pkgsjson/status_small.txt').read_text()
    json = converter.convert(txt)

    return HttpResponse(json)
