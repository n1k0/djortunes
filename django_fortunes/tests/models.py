import unittest
from utils import FortuneTransactionTestCase

from datetime import datetime
from django.test.testcases import TestCase, TransactionTestCase
from django_fortunes.models import Fortune

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