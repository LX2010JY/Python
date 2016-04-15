import socket
#AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
#join 将buffer序列的各个元素之间用''间隔连接成一个字符串
data = b''.join(buffer)
header,body = data.split(b'\r\n\r\n',1)
print(header)
with open('../file/sina.html','wb') as f:
    f.write(body)
with open('../file/header','wb')as f:
    f.write(header)
s.close()
