from django.test import TestCase
from djortunes.fortunes.templatetags.fortune_extras import fortunize

__test__ = {"doctest": """
fortunize() tests:

>>> fortunize('<niko> foo')
u'<dl><dt class="odd">niko</dt><dd><q>foo</q></dd>\n</dl>'
>>> fortunize(u'<niko> foo\\n<david> bar')
u'<dl><dt class="odd">niko</dt><dd><q>foo</q></dd>\n<dt class="even">david</dt><dd><q>bar</q></dd>\n</dl>'
"""}
