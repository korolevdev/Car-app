def encode(a, b, c):
	return int(a) << 24 | int(b) << 16 | 0 & 0xffff;

def decode(packet):
	a = packet >> 24
	b = (packet >> 16) & 0xff
	c = packet & 0xffff

	return a, b, c