# This file tests against three test vectors for the Base58 encoding protocol 
# https://tools.ietf.org/id/draft-msporny-base58-01.html#rfc.section.5

from sys import path
path.append('../')
from src.base58decode import b58decode

import unittest

class B58Decoder(unittest.TestCase):

	def test_decode_1(self):
		self.assertEqual(b"Hello World!", b58decode("2NEpo7TZRRrLZSi2U"))
	
	def test_decode_2(self):
		self.assertEqual(b"The quick brown fox jumps over the lazy dog.", b58decode("USm3fpXnKG5EUBx2ndxBDMPVciP5hGey2Jh4NDv6gmeo1LkMeiKrLJUUBk6Z"))
	
	def test_decode_3(self):
		self.assertEqual(b"(\x7f\xb4\xcd", b58decode("111233QC4"))

if __name__ == "__main__":
	unittest.main()
