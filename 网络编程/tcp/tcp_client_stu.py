# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:57
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : tcp_client_stu.py
# @Software: PyCharm

import socket

# 链接
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 链接服务器
tcpsocket.connect(('192.168.16.1', 8889))

# 输入
tcpsocket.send(input('请输入').encode())

# 接受
data = tcpsocket.recv(1024)
print(data)

# 关闭
tcpsocket.close()