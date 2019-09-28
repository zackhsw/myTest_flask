# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好

# 通过非阻塞io实现例子
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    # 不停地询问连接是否建立好，需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求
    while True:
        try:
            # 发送http请求，其实http是在tcp上加入了一些协议
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass


    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    # html_data = data.split("\r\n\r\n")[1]  # 截取请求头部分
    # print(html_data)
    print(data)
    client.close()

if __name__ == '__main__':
    get_url("http://www.baidu.com")
