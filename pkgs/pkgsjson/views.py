from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
import json
from pathlib import Path
import re
import demjson
#import dirtyjson # this one was completely useless


def home(request):
    #TODO fetch from command line
        #TODO split at every '\n\n' , or see if we can collapse/massage the data in some cleaner way
        #TODO use json.dumps to turn most of the content
    #TODO refactor to separate classes as needed
    #TODO figure out how Pythons 'unittest' works and implement
    #TODO test to destruction as needed
    #TODO polish code
    #TODO REMOVE THE DEBUG FLAG!!!!


    # get the text from a dump of status
    txt = Path('pkgsjson/status_small.txt').read_text()



    txt = txt.replace("\n\n", '[BREAK_TOKEN]')
    txt = txt.replace("\n .\n", '<br><br>')
    txt = txt.replace(" * ", '<li>')
    txt = txt.replace('https:',  '[PROTOCOL_TOKEN]')

    txt = txt.replace("\n ", '')
    # txt = txt.replace("\n", '')

    # txt = txt.replace("\n", ',')

    # this at least formats the keys correctly, still leaves the values as trash
    txt = re.sub("(\S+): ", r'"\1": ', txt)

    # value part
    txt = re.sub(r': (\S+.+)', r':"\1"', txt)
    # txt = re.sub(r': (\S+.+)', r':"REPLACED",\n', txt)

    # txt = txt.replace("\n", '<br>')
    # txt = txt.replace("[BREAK_TOKEN]", '},\n\n')

    txt = '{\n' + txt + '\n}'

    return HttpResponse(txt)

# deliniate the beginning and end of the package string with '{' and '},'
def json_encapsulate(txt):
    return txt.replace('"Package":', "{\"Package\":").replace("\n\n", "\n},\n")

#def json_