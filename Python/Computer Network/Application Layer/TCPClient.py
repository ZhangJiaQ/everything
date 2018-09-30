from socket import *

# 配置服务器地址与端口号
serverName = "127.0.0.1"
serverPort = 12000

# AF_INET 使用IPv4, SOCK_STREAM 使用TCP套接字
clientSocket = socket(AF_INET, SOCK_STREAM)

# 进行三次握手
clientSocket.connect((serverName, serverPort))

# 输入要传输的内容
sentence = bytes( input("请输入你要传输的字母\n"), encoding="utf-8")

# 发送并接收传回的值
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)

print(modifiedSentence)
# 关闭TCP连接 四次挥手
clientSocket.close()