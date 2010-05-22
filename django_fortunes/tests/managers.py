import unittest
import time

from utils import FortuneTransactionTestCase
from datetime import datetime
from django.test.testcases import TestCase, TransactionTestCase
from django_fortunes.models import Fortune

class FortuneManagerTest(FortuneTransactionTestCase):
    def test_latest(self):
        latest = Fortune.objects.latest()
        self.assertEqual(len(latest), 3)
        self.assertEqual(latest[0].author.username, 'Dude')
        self.assertEqual(latest[0].title, u'Another One')
        self.assertEqual(latest[1].author.username, 'NiKo')
        self.assertEqual(latest[1].title, u'A funny one')
        self.assertEqual(latest[2].author.username, 'NiKo')
        self.assertEqual(latest[2].title, u'My first fortune')
    
    def test_latest_by_author(self):
        latest_from_niko = Fortune.objects.latest_by_author('NiKo')
        self.assertEqual(len(latest_from_niko), 2)
        self.assertEqual(latest_from_niko[0].author.username, 'NiKo')
        self.assertEqual(latest_from_niko[0].title, u'A funny one')
        self.assertEqual(latest_from_niko[1].author.username, 'NiKo')
        self.assertEqual(latest_from_niko[1].title, u'My first fortune')
    
    def test_published(self):
        latest = Fortune.objects.published()
        self.assertEqual(len(latest), 3)
        f = self.create('foo', content='bar', pub_date=datetime.fromtimestamp(time.time() + 86400))
        new_latest = Fortune.objects.published()
        self.assertEqual(len(new_latest), 3)

    def test_top_authors(self):
        top_authors = Fortune.objects.top_authors()
        self.assertEqual(len(top_authors), 2)
        self.assertEqual(top_authors[0]['author__username'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 2)
        self.assertEqual(top_authors[1]['author__username'], 'Dude')
        self.assertEqual(top_authors[1]['nb'], 1)
        f = self.create(title='new one', author='NiKo')
        top_authors = Fortune.objects.top_authors()
        self.assertEqual(len(top_authors), 2)
        self.assertEqual(top_authors[0]['author__username'], 'NiKo')
        self.assertEqual(top_authors[0]['nb'], 3)
        self.assertEqual(top_authors[1]['author__username'], 'Dude')
        self.assertEqual(top_authors[1]['nb'], 1)
