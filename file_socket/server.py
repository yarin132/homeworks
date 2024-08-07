import os
import socket
import protocol

file_holder = "files\\"  # write here the place where the server holds the files


def upload(data):
    data = data.split("_")
    f = open(file_holder + data[0], "w")
    print(data[1])
    f.write(data[1])
    f.close()


def remove(file1):
    print(file1)
    if os.path.exists(file_holder + file1):
        os.remove(file_holder + file1)


def download(file_name, client_socket):
    if os.path.exists(file_holder + file_name):
        with open(file_holder + file_name, "r") as file:
            client_socket.send(protocol.create_msg(file.read()).encode())


def server_functions(data, client_socket):
    if data[0] == "u":  # upload
        upload(data[1:])
    elif data[0] == "r":  # remove
        remove(data[1:])
    elif data[0] == "d":
        download(data[1:], client_socket)
    elif data == "e":
        return False
    return True


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.SERVER_PORT))
    server_socket.listen()
    print("Server is up and running")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected from {client_address}")
        while True:
            data = protocol.get_msg(client_socket)
            if data is not None:
                if not server_functions(data, client_socket):
                    break
        client_socket.close()
        print("Client disconnected")


if __name__ == '__main__':
    main()
