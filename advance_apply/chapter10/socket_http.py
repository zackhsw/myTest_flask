# request --> urlib --> socket
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
    client.connect((host, 80))

    # 发送http请求，其实http是在tcp上加入了一些协议
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
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
