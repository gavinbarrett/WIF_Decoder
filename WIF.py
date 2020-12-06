from base58 import b58decode
from binascii import hexlify

input_bytes = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'

# decode the WIF from base58 to hexadecimal
byte_values = hexlify(b58decode(input_bytes))

# strip off the last four bytes (eight characters)
byte_values = byte_values[:-8]

# remove the leading byte
byte_values = byte_values[2:]

# drop the last byte if the public key is compressed
if input_bytes[0] == 'K' or input_bytes == 'L':
	byte_values = byte_values[:-2]

print(byte_values)
