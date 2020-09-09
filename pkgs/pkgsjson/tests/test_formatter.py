from django.test import TestCase

from pkgs.pkgsjson.formatconverter import FormatConverter


# So, i never actually got these to run, i have a misconfiguration somewhere, and couldn't figure out what in time.
class TestFormatConverter(TestCase):

    def testJsonPrettify(self):
        formatter = FormatConverter()
        fugly_string = '{"foo"    :     "bar",}'
        expected_string = '{"foo":  "bar"}'

        self.assertEquals(expected_string, formatter.json_prettify(fugly_string))

    # We expect non-compliant imput to throw a caught exception and return the original input
    def testJsonPrettifyFallback(self):
        formatter = FormatConverter()
        fugly_string = 'NOT!"actually"_valid: "json"'
        self.assertEquals(fugly_string, formatter.json_prettify(fugly_string))

