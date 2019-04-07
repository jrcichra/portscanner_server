import socket
import threading
import json
import itertools as it

server_port = 5555


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
    if client_address == '144.217.81.98':  # this is to prevent a chain reaction
        for port in it.chain(range(1, server_port), range(server_port+1, 65536)):
            res = scan_port(client_address, port)
            if(res):
                o['open'].append(port)
    else:
        for port in range(1, 65536):
            res = scan_port(client_address, port)
            if(res):
                o['open'].append(port)

    j = json.dumps(o, indent=4)
    print(j)
    client_socket.sendall(j.encode())
    client_socket.close()


if __name__ == '__main__':

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

        t = threading.Thread(target=check_client, args=(
            client_socket, client_address[0]))
        t.start()
