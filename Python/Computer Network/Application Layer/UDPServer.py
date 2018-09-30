from socket import *

# 设定端口号，初始化一个socket对象
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定端口号
serverSocket.bind(("", serverPort))

while True:
    print("1")
    # 接收参数，大写后返回给用户端
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)