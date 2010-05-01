import unittest

from utils import FortuneTransactionTestCase

class SimpleTest(FortuneTransactionTestCase):
    def test_404(self):
        response = self.client.get('/show/2020/4/2/won-t-exist/')
        self.failUnlessEqual(response.status_code, 404)

    def test_index(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        fortunes = response.context['fortune_list']
        self.failUnlessEqual(len(fortunes), 3)
        self.assertEqual(fortunes[0].pub_date > fortunes[1].pub_date > fortunes[2].pub_date, True)

    def test_top(self):
        response = self.client.get('/top/')
        self.failUnlessEqual(response.status_code, 200)
        fortunes = response.context['fortune_list']
        self.failUnlessEqual(len(fortunes), 3)
        self.assertEqual(fortunes[0].votes, 3)
        self.assertEqual(fortunes[1].votes, 2)
        self.assertEqual(fortunes[2].votes, 1)

    def test_worst(self):
        response = self.client.get('/worst/')
        self.failUnlessEqual(response.status_code, 200)
        fortunes = response.context['fortune_list']
        self.failUnlessEqual(len(fortunes), 3)
        self.assertEqual(fortunes[0].votes, 1)
        self.assertEqual(fortunes[1].votes, 2)
        self.assertEqual(fortunes[2].votes, 3)