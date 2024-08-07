LENGTH_FIELD_SIZE = 20
SERVER_PORT = 88


def create_msg(data):
    return str(len(data)).zfill(LENGTH_FIELD_SIZE) + data


def get_msg(my_socket):
    word_length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if word_length.isdigit():
        user = my_socket.recv(int(word_length)).decode()
        return user
    return "error"
