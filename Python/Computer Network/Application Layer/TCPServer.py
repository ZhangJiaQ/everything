from socket import *

# 设置端口，设置为IPv4与TCP连接
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
# 绑定端口号
serverSocket.bind(("", serverPort))
# 设置最大连接数
serverSocket.listen(1)

while 1:
    print(11)
    # 接受参数
    connectionSocket, addr = serverSocket.accept()
    # 操作数据并返回
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    # 关闭连接
    connectionSocket.close()