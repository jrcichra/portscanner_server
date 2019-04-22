import socket
import threading
import json
import re
import signal
import sys

reg = r'^([\w]+.[\w]+)'
server_port = 5555


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def scan_port(client_address, port):
    check_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    check_socket.settimeout(.001)
    res = check_socket.connect_ex((client_address, port))
    check_socket.close()
    if(res == 0):
        return True
    else:
        return False


def check_client(client_socket, client_address):
    o = {}
    o['ip'] = client_address
    o['open'] = []
    for port in range(1, 65536):
        status = '\rscanning port: ' + str(port)
        client_socket.sendall(status.encode())
        res = scan_port(client_address, port)
        if(res):
            found = '\n open: ' + str(port) + '\n'
            client_socket.sendall(found.encode())

    client_socket.close()


if __name__ == '__main__':
    # control c listener
    signal.signal(signal.SIGINT, signal_handler)
    # setup the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", server_port))
    server_socket.listen()
    # handle incoming connections
    while True:
        print("Ready for a client...")
        client_socket, client_address = server_socket.accept()

        print("Got a connection from " + str(client_address[0]))

        request = client_socket.recv(1024)
        print(request)
        if('portscan' in request.decode()):
            t = threading.Thread(target=check_client, args=(
                client_socket, client_address[0]))
            t.start()
        else:
            client_socket.close()
