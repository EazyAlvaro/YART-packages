import json
import re
import yaml

class FormatConverter:

    # performs all the internal steps to convert the raw text into valid JSON
    def convert(self, txt: str) -> str:
        # Since we are converting for web consumption, HTML seems permisable
        txt = self.cleanup_non_json_character(txt)

        # Format the quotes around key/value pairs, ignoring the cases inside the value text that contain colons
        txt = self.json_format_key_value_txt(txt)

        # begin and end with the approprite curlies and brackets
        txt = self.json_enclose(txt)

        # Does what it says on the box
        txt = self.json_prettify(txt)
        return txt

    # Cast the text to YAML (a superset of JSON) and back to text JSON, YAML is more permissive with trailing commas
    # but it comes out squeeky clean in the end
    #
    def json_prettify(self, txt: str) -> str:
        try:
            data = yaml.load(txt)
            txt = json.dumps(data, indent=4)
        except:
            1 == 1  # does nothing, but i can't leave it empty
        return txt

    def cleanup_non_json_character(self, txt: str) -> str:
        txt = txt.replace("\n .\n", '<br><br>')
        txt = txt.replace(" * ", '<li>')
        txt = txt.replace("\n ", '')
        return txt

    # Format the key and value of a single pair (the first) to have JSON conformant double quotes
    #
    # Admittedly, using this in a loop is a bit of a cheat as i couldn't figure out a clean RegEx.
    # But for time investment, this is the biggest bang for my buck
    def json_format_key_value_line(self, txt: str) -> str:
        # Format the FIRST key, This is because there are colons in the text
        txt = re.sub("(^\S+): ", r'"\1": ', txt)
        # Format the value
        txt = re.sub(r': (\S+.+)', r': "\1",', txt)
        return txt

    # Format a large string containing multiple key/value pairs into JSON
    def json_format_key_value_txt(self, txt: str) -> str:
        txt_looped = ''
        for line in txt.split('\n'):
            txt_looped = txt_looped + self.json_format_key_value_line(line) + '\n'
        return txt_looped

    def json_enclose(self, txt: str) -> str:
        new_txt = txt.replace('"Package"', '{\n"Package"'). \
            replace("\n\n", "\n},\n"). \
            replace(",\n}", "\n}")
        return '[\n' + new_txt + '\n]'
