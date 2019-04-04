#  Kirsty Russell
#  CS 4720
#  Assignment 3
#  Professor Setzer
#  February 12, 2019

from socket import socket
from collector import Collector

PORT = 12345

# Creates Collector
collector = Collector()
# Get a socket object
listener = socket()
# We are a server, we request to use a particular port
listener.bind(('', PORT))

# We listen
listener.listen(0)

while True:
    # The following function call waits until there is a connection
    # When a connection is made, this function returns information about the connection.
    (conn, address) = listener.accept()
    # Conn is a socket that we will use to communicate with the client

    data_bytes = b""

    receivedB = conn.recv(2048)
    while len(receivedB) > 0:
        data_bytes += receivedB
        receivedB = conn.recv(2048)

    data_string = data_bytes.decode("UTF-8")

    print("data_string", data_string)

    if len(data_string) == 0:
        reply = "Error: empty command"
    else:
        cmd = data_string[0]            # first character
        parameter = data_string[1:]     # the rest
        # Adds the value to the collector
        if cmd == 'A':
            try:
                v = float(parameter)
                collector.add(v)
                reply = "OK " + parameter + " added"
            except ValueError as ve:
                reply = "Error"
        # Asks for the average
        elif cmd == 'a':
            reply = str(collector.average())
        # Asks for the count
        elif cmd == 'c':
            reply = str(collector.count())
        # Asks for the standard deviation
        elif cmd == 'd':
            reply = str(collector.standard_deviation())
        # Asks for the sum of squares
        elif cmd == 'q':
            reply = str(collector.sum_squares())
        # Asks for the sum
        elif cmd == 's':
            reply = str(collector.sum())
        # Asks for the variance
        elif cmd == 'v':
            reply = str(collector.variance())
        # Resets the collector
        elif cmd == 'z':
            collector = Collector()
            reply = "OK: Collector reset"
        else:
            reply = "Error"

    conn.sendall(reply.encode("UTF-8"))
    conn.shutdown(1)

conn.close()

listener.close()
