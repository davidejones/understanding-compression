import unittest

from vlc import encode, decode


class CompressionTests(unittest.TestCase):
    def test_encode(self):
        self.assertEqual('', encode('TOBEORNOTTOBEORTOBEORNOT'))
