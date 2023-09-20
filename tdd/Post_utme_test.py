import unittest

from tdd.Post_utme import Post_utme


class Post_utme_test(unittest.TestCase):
    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(2000, self.post_utme.get_price(4))

    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(1800,self.post_utme.get_price(9))


    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(1600,self.post_utme.get_price(25))

    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(1500, self.post_utme.get_price(45))


    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(1300,self.post_utme.get_price(50))

    def test_number_of_copies(self):
        self.post_utme = Post_utme()
        self.assertEqual(1200,self.post_utme.get_price(120))