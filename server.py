import socket
import sys
import operator
import parser

host = ''
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

print "Listening for client . . ."
conn, address = server_socket.accept()
print "Connected to client at ", address

while True:
    output = conn.recv(2048)
    if output.strip() == "disconnect":
        conn.close()
        sys.exit("Received disconnect message.  Shutting down.")
        conn.send("dack")
        
    elif output:
        print output
        values = parser.firstParser(output)
        orientation = (values[1]-77)/57.0
        totalSteps = values[2]
        print orientation
        print totalSteps
        
