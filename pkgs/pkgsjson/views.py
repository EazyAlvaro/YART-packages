from django.shortcuts import render
from django.http import HttpResponse
import json
from pathlib import Path
import re
import yaml

def home(request):
    # DONE fetch from command line
    # DONE split at every '\n\n' , or see if we can collapse/massage the data in some cleaner way
    # DONE use json.dumps to turn most of the content into compliant JSON
    # TODO refactor to separate classes as needed
    # TODO figure out how Pythons 'unittest' works and implement
    # TODO test to destruction as needed
    # TODO polish code
    # TODO REMOVE THE DEBUG FLAG!!!!

    # get the text from a dump of status
    txt = Path('pkgsjson/status.txt').read_text()

    # Since we are converting for web consumption, HTML seems permisable
    txt = cleanup_non_json_character(txt)

    # Format the quotes around key/value pairs, ignoring the cases inside the value text that contain colons
    txt = json_format_key_value_txt(txt)

    # begin and end with the approprite curlies and brackets
    txt = json_enclose(txt)

    # Does what it says on the box
    txt = json_prettify(txt)

    return HttpResponse(txt)


# Cast the text to YAML (a superset of JSON) and back to text JSON, YAML is more permissive with trailing commas
# but it comes out squeeky clean in the end
#
def json_prettify(txt: str) -> str:
    try:
        data = yaml.load(txt)
        txt = json.dumps(data, indent=4)
    except:
        txt = txt  # does nothing, but i can't leave it empty
    return txt


def cleanup_non_json_character(txt: str) -> str:
    txt = txt.replace("\n .\n", '<br><br>')
    txt = txt.replace(" * ", '<li>')
    # txt = txt.replace('https:', '[PROTOCOL_TOKEN]')
    txt = txt.replace("\n ", '')
    return txt

# Format a large string containing multiple key/value pairs into JSON
def json_format_key_value_txt(txt: str) -> str:
    txt_looped = ''
    for line in txt.split('\n'):
        txt_looped = txt_looped + json_format_key_value_line(line) + '\n'
    return txt_looped


# Format the key and value of a single pair (to me technically accurate, the first) to have JSON conformant double quotes
#
# Admittedly, using this in a loop is a bit of a cheat as i couldn't figure out a clean RegEx.
# But for time investment, this is the biggest bang for my buck
def json_format_key_value_line(txt: str) -> str:
    # Format the FIRST key, This is because there are colons in the text
    txt = re.sub("(^\S+): ", r'"\1": ', txt)
    # txt = re.sub("(\S+): ", r'"\1": ', txt)

    # Format the value
    txt = re.sub(r': (\S+.+)', r': "\1",', txt)
    return txt


def json_enclose(txt: str) -> str:
    txt = txt.replace('"Package"', '{\n"Package"'). \
        replace("\n\n", "\n},\n"). \
        replace(",\n}", "\n}")
    return '[\n' + txt + '\n]'
