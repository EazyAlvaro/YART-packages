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



    # Since we are converting for web consumption, HTML seems permisable
    txt = txt.replace("\n .\n", '<br><br>')
    txt = txt.replace(" * ", '<li>')
    txt = txt.replace('https:',  '[PROTOCOL_TOKEN]')
    txt = txt.replace('"', 'ZZZ')

    txt = txt.replace("\n ", '')

    # Format the keys
    txt = re.sub("(\S+): ", r'"\1": ', txt)

    # Format the values. I tried putting it all in one regex,
    # but alas i did something wrong  and this is faster than teaching myself proper regex
    txt = re.sub(r': (\S+.+)', r': "\1",', txt)



    # begin and end with the approprite curlies and brackets
    txt = json_enclose(txt)

    # txt = json.encoder(txt)

    # data = json.loads(txt)
    # txt = json.dumps(data, indent=1)

    return HttpResponse(txt)


def json_enclose(txt: str) -> str:
    txt = txt.replace('"Package"', '{"Package"').\
        replace("\n\n", "\n},\n").\
        replace(",\n}", "\n}")
    return '[\n' + txt + '\n]'
