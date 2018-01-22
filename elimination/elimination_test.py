import unittest

from elimination import encode


class CompressionTests(unittest.TestCase):
    def test_encode_empty_list(self):
        self.assertMultiLineEqual(encode([]), '')

    def test_encode_string(self):
        with self.assertRaises(TypeError):
            encode("")

    def test_encode_list(self):
        self.assertEqual('101 110 001 011 11 10 1 0', encode([5, 7, 1, 4, 6, 3, 2, 0]))
