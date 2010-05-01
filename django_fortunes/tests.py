import unittest
from django.test.testcases import TestCase, TransactionTestCase
from datetime import datetime
from django_fortunes.models import Fortune

class FortuneExtraTest(TestCase):
    def test_fortunize(self):
        from django_fortunes.templatetags.fortune_extras import fortunize
        self.assertEquals(fortunize(u'<niko> foo'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<niko> foo\n<david> bar'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n<dt class="even">&lt;david&gt;</dt><dd><q>bar</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<script>foo</script>'), u'<dl><dt class="odd">&lt;script&gt;</dt><dd><q>foo&lt;/script&gt;</q></dd>\n</dl>')

class FortuneModelTest(TransactionTestCase):
    def create(self, title, author='Anon', content='', pub_date=datetime.now()):
        f = Fortune(title=title, author=author, content=content, pub_date=pub_date)
        f.save()
        return f

    def test_check_slug(self):
        f1 = self.create(title='plop', pub_date=datetime.now())
        self.assertEquals(f1.slug, 'plop')
        f2 = self.create(title='plop', pub_date=datetime.now())
        self.assertEquals(f2.slug, '1-plop')
        f3 = self.create(title='plop', pub_date=datetime.now())
        self.assertEquals(f3.slug, '2-plop')
        Fortune.objects.get(slug='plop').delete()

    def test_top_contributors(self):
        top_authors = Fortune.objects.top_authors(2)
        self.assertEqual(len(top_authors), 2)
        self.assertEqual(top_authors[0]['author'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 2)
        self.assertEqual(top_authors[1]['author'], 'Dude')
        self.assertEqual(top_authors[1]['nb'], 1)
        f = self.create(title='new one', author='NiKo')
        top_authors = Fortune.objects.top_authors(1)
        self.assertEqual(len(top_authors), 1)
        self.assertEqual(top_authors[0]['author'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 3)
