package ipc

import(
	"encoding/json"
)

type IpcClient struct {
	coon chan string        //定义一个IpcClinet
}

func NewIpcClient(server *IpcServer) *IpcClient {
	c := server.Connect()

	return &IpcClient{c}
}

func (client *IpcClient) Call(method, params string) (resp *Response, err error) {
	//给IpcClient定义一个Call方法，接受params,method为参数,
	//返回一个名为resp的Response类型和err
	//会将调用信息封装成一个JSON格式的字符串返回给channel,并等待获取反馈

	req := &Request{method, params} //根据接受的method和params构成一个Request
	
	var b []byte //创建一个名为b的字符数组
	b, err = json.Marshal(req)
	if err != nil {
		return	
	}

	client.coon <- string(b)  //将b写入到channel内
	str := <-client.coon      // 初始化一个单向channel

	var resp1 Response
	err = json.Unmarshal([]byte(str), &resp1)
	resp = &resp1
	
	return	
}

func (client *IpcClient)Close() {
	client.coon <- "CLOSE"
}


