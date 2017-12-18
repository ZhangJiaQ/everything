package ipc

import(
	"encoding/json"
	"fmt"
)

type Request struct {         //构建一个Requst类型
	Method string "method"
	Params string "params"
}
  
type Response struct {        //构建一个Response类型
	Code string "code"
	Body string "body"
}

type Server interface {         //  构建一个Server接口
	Name() string
	Handle(method, params string) *Response
}

type IpcServer struct {        //构建一个IpcServer类型
	Server
}

func NewIpcServer(server Server) *IpcServer {    //构建一个NewIpServer函数
	return &IpcServer{server}                    //这个函数接收一个server返回一个在IpcServer下的
}												 //Server接口

func (server *IpcServer)Connect() chan string{
	session := make(chan string, 0)               //构建一个session的channel
	
	go func(c chan string) {					 //构建一个匿名并行函数，接受channel作为参数
		for {
			request := <-c						 //从c中取出request
			if request == "CLOSE"{               //如果需要关闭则关闭这个链接
				break
			}
			
			var req Request		
			err := json.Unmarshal([]byte(request), &req)  //将struct对象序列化到json对象中
			if err != nil {
				fmt.Println("Invalid request format:", request)
			}
			
			resp := server.Handle(req.Method, req.Params)

			b,err := json.Marshal(resp)
			
			c <- string(b)			
		}
		
		fmt.Println("Session closed.")
	}(session)

	fmt.Println("A now session has been created successfully")
	
	return session
}
