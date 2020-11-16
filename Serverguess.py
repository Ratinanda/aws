import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 49000)
# print >>sys.stderr, 'starting up on %s port %s' % server_address*/
sock.bind(server_address)
sock.listen(1)
while True:

