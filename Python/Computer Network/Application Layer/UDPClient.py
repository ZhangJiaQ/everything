from socket import *


# 设定目标地址和端口号
serverName = "localhost"
serverPort = 12000

# AF_INET 表示底层网络使用了IPv4， SOCK_DGRAM表示它是一个UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = bytes(input("请输入要发送的内容\n"), encoding='utf-8')

# 发送消息
clientSocket.sendto(message, (serverName, serverPort))

# 接收消息 缓存长度2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(str(modifiedMessage))

clientSocket.close()
