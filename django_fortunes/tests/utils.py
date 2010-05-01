import unittest

from datetime import datetime
from django.test.testcases import TransactionTestCase
from django_fortunes.models import Fortune

class FortuneTransactionTestCase(TransactionTestCase):
    def create(self, title, author='Anon', content='', pub_date=datetime.now()):
        f = Fortune(title=title, author=author, content=content, pub_date=pub_date)
        f.save()
        return f