package cg

import (
	"encoding/json"
	"errors"
	"sync"

	"ipc"
)

var _ ipc.Server = &CenterServer{}   //确认实现了server借口

type Message struct {   //构造出信息类型，由from to content构成
	From string "from"
	To string "to"
	Content string "content"
}

type CenterServer struct {   //构造出CenterServer类型
	servers map[string] ipc.Server
	players []*Player
	rooms []*Room
	mutex sync.RWMutex
}

func NewCenterServer() *CenterServer {
	servewrs := make(map[string] ipc.Server) //初始化一个map
	players := make([]*Player, 0)   //初始化一个数组切片，长度为0
	
	return &CenterServer{servers:servers, player:player}
}

func (server *CenterServer)addPlayer(params string) error {  //给CenterServer类型添加addPlayer方法
	player := NewPlayer()
	
	err := json.Unmarshal([]byte(params), &player) //将取得的json解码
	if err != nil {
		return err
	}

	server.mutex.Lock()
	defer server.mutex.Unlock()

	server.players = append(server.players, player)

	return nil
}

func (server *CenterServer)removePlayer(params string) error {   //给CenterServer类型添加removePlayer方法
	//给server通道加锁 遍历当前用户名单 进行删除操作
	server.mutex.Lock()
	defer server.mutex.Unlock()

	for i, v := range server.players {
		if v.Name == params {
			server.players = make([]*Player, 0)
		} else if i == len(server.players) - 1 {
			server.players = server.players[:i-1]
		} else if i == 0 {
			server.players = server.players[1:]
		} else {
			server.players = append(server.players[:i-1], server.players[:i+1]...)
		} 
		return nil
		}
	}	
	return errors.New("Player not found")
}

func (server *CenterServer) listPlayer(params string)(Players string, err error) {  

	//返回目前玩家列表 //给CenterServer类型添加listPlayer方法
	
	server.mutex.RLock()  //加一个读锁，但不影响别的进程去读，但该资源在锁释放前不能进行写操作
	defer server.mutex.RUnlock()

	if len(server.players) > 0 {
		b, _ := json.Marshal(server.players)		
		players = string(b)
	} else {
		err = errors.New("No player online.")
	}
	return
}

func (server *CenterServer) broadcast(params string) error {	    ////给CenterServer类型添加broadcast方法

	var message Message   //定义一个类型为Message的变量
	err := json.Unmarshal([]byte(params), &message)  //将取得的params解编码
	if err != nil {
		return err
	}

	server.mutex.Lock()   //锁！
	defer server.mutex.Unlock()

	if len(server.players) > 0 {
		for _, player := range server.players {
			player.mq <- &message      //如果有玩家在线的话，给player内定义的message消息队列传入一条消息
		}
	} else {
		err = errors.New("No player online")  
	}
}

func (server *CenterServer)Handle(method, params string) *ipc.Response {
	//命令行解析工具
	switch method {
		case "addplayer":
			err := server.addPlayer(params)
			if err != nil {
				return &ipc.Response{Code:err.Error()}
			}
		case "removeplayer":
			err := server.removePlayer(params)		
			if err != nil {
				return &ipc.Response{Code:err.Error()}
			}
		case "listplayer":
			err, player := server.listPlayer(params)
			if err != nil {
				return &ipc.Response{Code:err.Error()}
			}
			return &ipc.Response{"200", players}
		case "broadcast":
			err := server.broadcast(params)
			if err != nil {
				return &ipc.Response{Code:err.Error()}
			}
			return &ipc.Response{Code:"200"}
			default:
				return &ipc.Response{Code:"404", Body:method + ":" + params}
	}
	return &ipc.Response{Code:"200"}
}

func (server *CenterServer) Name() string {
	return "CenterServer"
}
