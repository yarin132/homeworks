import socket
import protocol
import os


def upload(my_socket,func):
    name_file = input("enter file name: ")
    path_file = input("enter file path: ")
    if os.path.exists(path_file):
        with open(path_file, "r") as file_data:
            my_socket.send(protocol.create_msg(f"{func}{name_file}_{file_data.read()}").encode())


def download(my_socket,func):
    file = input("enter file name: ")
    my_socket.send(protocol.create_msg(func+file).encode())
    data = protocol.get_msg(my_socket)
    with open(file, "w") as file:
        file.write(data)


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.SERVER_PORT))
    while True:
        print("enter what you want to do")
        func = input("u to upload, r to remove, d to download, e to close client")
        if "r" == func:
            file = input("enter file name: ")
            my_socket.send(protocol.create_msg(func + file).encode())
        elif "u" == func:
            upload(my_socket,func)
        elif "d" == func:
            download(my_socket,func)
        elif "e" == func:
            break
    print("shutting down")
    my_socket.send(protocol.create_msg("e").encode())
    my_socket.close()



if __name__ == "__main__":
    main()



