def encode(a, b, c):
	return int(a) << 24 | int(b) << 16 | 0 & 0xffff;

def decode(packet):
	a = packet >> 24
	b = (packet >> 16) & 0xff
	c = packet & 0xffff

	return a, b, c

def get_pitch(quat):
	q0, q1, q2, q3 = quat
    q0 = q0 / 16384.0
    q1 = q1 / 16384.0
    q2 = q2 / 16384.0
    q3 = q3 / 16384.0
    return -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))

def get_roll(quat):
	q0, q1, q2, q3 = quat
    q0 = q0 / 16384.0
    q1 = q1 / 16384.0
    q2 = q2 / 16384.0
    q3 = q3 / 16384.0
    return math.atan2(2.0 * (q0 * q1 + q2 * q3), 1.0 - 2.0 * (q1 * q1 + q2 * q2))