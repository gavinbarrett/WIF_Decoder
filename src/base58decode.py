from binascii import hexlify

# base58 alphabet
alphabet = {
	'1':0,'2':1,'3':2,'4':3,
	'5':4,'6':5,'7':6,'8':7,
	'9':8,'A':9,'B':10,'C':11,
	'D':12,'E':13,'F':14,'G':15,
	'H':16,'J':17,'K':18,'L':19,
	'M':20,'N':21,'P':22,'Q':23,
	'R':24,'S':25,'T':26,'U':27,
	'V':28,'W':29,'X':30,'Y':31,
	'Z':32,'a':33,'b':34,'c':35,
	'd':36,'e':37,'f':38,'g':39,
	'h':40,'i':41,'j':42,'k':43,
	'm':44,'n':45,'o':46,'p':47,
	'q':48,'r':49,'s':50,'t':51,
	'u':52,'v':53,'w':54,'x':55,
	'y':56,'z':57
}

def b58decode_bytes(string):
	''' decode each byte with the alphabet map '''
	carry = 0
	for char in string:
		carry = (carry * 58) + alphabet[char]
	return carry

def b58decode(string):
	length = len(string)
	acc = b58decode_bytes(string)
	decoded = []
	while acc > 0:
		acc, mod = divmod(acc, 256)
		decoded.append(mod)
	return bytes(reversed(decoded))

def strip_bytes(byte_string):
	# strip the first and last four bytes from the buffer
	byte_string = byte_string[2:-8]
	# strip an additional byte from the end if pubkey is compressed
	if byte_string[0] == 'K' or byte_string[0] == 'L':
		return byte_string[:-2]
	return byte_string

def b58checkdecode(wif_key):
	# convert the WIF key into hexadecimal
	return strip_bytes(hexlify(b58decode(wif_key)))

def decode_key():
	# decode a user provided WIF key
	key = input('Enter your WIF private key: ')
	decoded_key = b58checkdecode(key)
	print('Your private key is: ' + decoded_key.decode())

if __name__ == "__main__":
	decode_key()
