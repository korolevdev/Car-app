def encode(a, b, c):
	return int(a) << 24 | int(b) << 16 | int(c) & 0xffff;

def decode(packet):
	a = packet >> 24
	b = (packet >> 16) & 0xff
	c = packet & 0xffff

	if c & 0x8000:
		c = c - 0x10000
	return a, b, c