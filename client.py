# Don't forget to change this file's name before submission.
import sys
import os
import enum
from common import TftpProcessor, check_file_name

def setup_sockets(address):
    """
    Socket logic MUST NOT be written in the TftpProcessor
    class. It knows nothing about the sockets.

    Feel free to delete this function.
    """
    pass


def do_socket_logic():
    """
    Example function for some helper logic, in case you
    want to be tidy and avoid stuffing the main function.

    Feel free to delete this function.
    """
    pass


def parse_user_input(address, operation, args=None):
    # Your socket logic can go here,
    # you can surely add new functions
    # to contain the socket code. But don't
    # add socket code in the TftpProcessor class.
    # Feel free to delete this code as long as the
    # functionality is preserved.
    if operation == "push":
        print(f"Attempting to upload [{args}]...")
        pass
    elif operation == "pull":
        print(f"Attempting to download [{args}]...")
        pass


def main():
    """
     Write your code above this function.
    if you need the command line arguments
    """
    print("*" * 50)
    print("[LOG] Printing command line arguments\n", ",".join(sys.argv))
    check_file_name()
    print("*" * 50)

    # This argument is required in both client and server.
    # For a server, this means the IP that the server socket
    # will use.
    # For a client, it means the IP of the server.
    ip_address = sys.argv[1]

    # The following code is valid if you're implementing a client
    # if you're implementing a server, remove those arguments and
    # their usage.
    try:
        operation = sys.argv[2]
        file_name = sys.argv[3]
        # Modify this as needed.
        parse_user_input(ip_address, operation, file_name)
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()
