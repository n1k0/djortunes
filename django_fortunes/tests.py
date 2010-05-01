import unittest
from datetime import datetime
from django.test.testcases import TestCase, TransactionTestCase
from django_fortunes.models import Fortune

class FortuneExtraTest(TestCase):
    def test_fortunize(self):
        from django_fortunes.templatetags.fortune_extras import fortunize
        self.assertEquals(fortunize(u'<niko> foo'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<niko> foo\n<david> bar'), u'<dl><dt class="odd">&lt;niko&gt;</dt><dd><q>foo</q></dd>\n<dt class="even">&lt;david&gt;</dt><dd><q>bar</q></dd>\n</dl>')
        self.assertEquals(fortunize(u'<script>foo</script>'), u'<dl><dt class="odd">&lt;script&gt;</dt><dd><q>foo&lt;/script&gt;</q></dd>\n</dl>')

class FortuneTransactionTestCase(TransactionTestCase):
    def create(self, title, author='Anon', content='', pub_date=datetime.now()):
        f = Fortune(title=title, author=author, content=content, pub_date=pub_date)
        f.save()
        return f

class FortuneTest(FortuneTransactionTestCase):
    def test_check_slug(self):
        f1 = self.create(title='plop')
        self.assertEquals(f1.slug, 'plop')
        f2 = self.create(title='plop')
        self.assertEquals(f2.slug, '1-plop')
        f3 = self.create(title='plop')
        self.assertEquals(f3.slug, '2-plop')
        f2.delete()
        f4 = self.create(title='plop')
        self.assertEquals(f4.slug, '1-plop')
        Fortune.objects.get(slug='plop').delete()

class FortuneManagerTest(FortuneTransactionTestCase):
    def test_latest(self):
        latest = Fortune.objects.latest()
        self.assertEqual(len(latest), 3)
        self.assertEqual(latest[0].author, 'NiKo')
        self.assertEqual(latest[0].title, u'A funny one')
        self.assertEqual(latest[1].author, 'Dude')
        self.assertEqual(latest[1].title, u'Another One')
        self.assertEqual(latest[2].author, 'NiKo')
        self.assertEqual(latest[2].title, u'My first fortune')
    
    def test_latest_by_author(self):
        latest_from_niko = Fortune.objects.latest_by_author('NiKo')
        self.assertEqual(len(latest_from_niko), 2)
        self.assertEqual(latest_from_niko[0].author, 'NiKo')
        self.assertEqual(latest_from_niko[0].title, u'A funny one')
        self.assertEqual(latest_from_niko[1].author, 'NiKo')
        self.assertEqual(latest_from_niko[1].title, u'My first fortune')

    def test_top_authors(self):
        top_authors = Fortune.objects.top_authors()
        self.assertEqual(len(top_authors), 2)
        self.assertEqual(top_authors[0]['author'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 2)
        self.assertEqual(top_authors[1]['author'], 'Dude')
        self.assertEqual(top_authors[1]['nb'], 1)
        f = self.create(title='new one', author='NiKo')
        top_authors = Fortune.objects.top_authors()
        self.assertEqual(len(top_authors), 2)
        self.assertEqual(top_authors[0]['author'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 3)
        self.assertEqual(top_authors[1]['author'], 'Dude')
        self.assertEqual(top_authors[1]['nb'], 1)
