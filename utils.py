def encode(a, b, c):
	try:	
		return int(a) << 24 | int(b) << 16 | int(c) & 0xffff;
	except ValueError:
		print "Encode only int"

def decode(packet):
	a = packet >> 24
	b = (packet >> 16) & 0xff
	c = packet & 0xffff

	return a, b, c

def check_int(str):
    try:
        int(str)
        return True
    except:
        return False

def perform_json(real_speed, route, teor_speed):
	return '{"real_speed":"' + str(real_speed) + '","route":' + str(route) + ',"teor_speed":"' + str(teor_speed) + '"}'
