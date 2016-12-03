def get_android_commands(connection):
	sock = socket.socket()
	sock.bind(('', 9092))

	while True:
		sock.listen(1)
		conn, addr = sock.accept()

		print 'connected:', addr

		data = conn.recv(1024)

		if data:
			connection.send(str(encode(data, 50)))

		conn.close() 