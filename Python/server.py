import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.222', 80)
print >>sys.stderr, 'Iniciando server %s puerto %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'esperando por conexion...'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'conectado con', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'recibido "%s"' % data
            if data:
                print >>sys.stderr, 'enviando datos al cliente'
                #connection.sendall(data)
            else:
                print >>sys.stderr, 'no hay mas datos de', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()