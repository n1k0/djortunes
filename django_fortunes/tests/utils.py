import unittest

from datetime import datetime
from django.contrib.auth.models import User
from django.test.testcases import TransactionTestCase
from django_fortunes.models import Fortune

class FortuneTransactionTestCase(TransactionTestCase):
    def create(self, title, author='Anon', content='', pub_date=datetime.now()):
        try:
            user = User.objects.get(username=author)
        except User.DoesNotExist:
            user = User(username=author, email='foo@bar.com', is_active=True)
            user.save()
        f = Fortune(title=title, author=user, content=content, pub_date=pub_date)
        f.save()
        return f