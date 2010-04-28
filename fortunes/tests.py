import unittest

class FortuneExtraTest(unittest.TestCase):
    def test_fortunize(self):
        from djortunes.fortunes.templatetags.fortune_extras import fortunize
        self.assertEquals(fortunize(u'<niko> foo'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<niko> foo\n<david> bar'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n<dt class="even">&lt;david&gt;</dt><dd><q>bar</q></dd>\n</dl>')

class FortuneModelTest(unittest.TestCase):
    def test_check_slug(self):
        import datetime
        from djortunes.fortunes.models import Fortune
        f1 = Fortune(title='plop', pub_date=datetime.datetime.now())
        f1.save()
        self.assertEquals(f1.slug, 'plop')
        f2 = Fortune(title='plop', pub_date=datetime.datetime.now())
        f2.save()
        self.assertEquals(f2.slug, '1-plop')
        f3 = Fortune(title='plop', pub_date=datetime.datetime.now())
        f3.save()
        self.assertEquals(f3.slug, '2-plop')