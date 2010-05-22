import unittest

from django.test.testcases import TestCase
from django_fortunes.templatetags.fortune_extras import fortunize, top_contributors

class FortuneExtraTest(TestCase):
    def test_fortunize(self):
        self.assertEquals(fortunize(u'<niko> foo'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<niko> foo\n<david> bar'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n<dt class="even">&lt;david&gt;</dt><dd><q>bar</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<script>foo</script>'), u'<dl><dt class="odd">&lt;script&gt;</dt><dd><q>foo&lt;/script&gt;</q></dd>\n</dl>')

    def test_top_contributors(self):
        authors = top_contributors()['authors'];
        self.assertEquals(len(authors), 2)
        self.assertEquals(authors[0]['author__username'], u'NiKo')
        self.assertEquals(authors[0]['nb'], 2)
        self.assertEquals(authors[1]['author__username'], u'Dude')
        self.assertEquals(authors[1]['nb'], 1)
        