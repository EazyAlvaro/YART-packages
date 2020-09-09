from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from .formatconverter import FormatConverter
import json

def jsonraw(request):
    converter = FormatConverter()

    # get the text from a dump of status
    txt = Path('pkgsjson/status.txt').read_text()
    json = converter.convert(txt)

    return HttpResponse(json)


def html(request):
    converter = FormatConverter()
    # Using a cropped version for the HTML
    txt = Path('pkgsjson/status_small.txt').read_text()
    json_txt = converter.convert(txt)
    package_data = json.loads(json_txt)

    return render(request, 'pkgsjson/template.html', context={'package_data': package_data})