import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


# 如何解决多用户连接 使用多线程方式
def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))


# 获取从客户端发送的数据
# 一次获取1k数据
while True:
    sock, addr = server.accept()

    # 用线程取处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print("main--",data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))

    # sock.send(f"hello { data.decode('utf8') }".encode("utf8"))
    # sock.close()
    # server.close()
