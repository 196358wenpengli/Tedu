from socket import *


def recv_image(conn):
    fw = open("20211209.jpeg", 'wb')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        fw.write(data)

    fw.close()


def main():
    sock = socket()
    sock.bind(("0.0.0.0", 8888))
    sock.listen(5)
    conn, addr = sock.accept()
    print("connect from", addr)
    recv_image(conn)
    conn.close()
    sock.close()


if __name__ == '__main__':
    main()
