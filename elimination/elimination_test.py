import unittest
from .elimination import encode, decode


class CompressionTests(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertMultiLineEqual(encode(''), '')
