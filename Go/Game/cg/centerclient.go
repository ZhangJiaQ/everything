package cg

import(
	"errors"
	"encoding/json"
	
	"ipc"
)

type CenterClient struct {
	*ipc.IpcClient    //匿名组合IpcClient 所以可以直接在代码中调用IpcClient的功能
}

func (client *CenterClient) AddPlayer(player *Player) error {
	//给CenterClient增加AddPlayer方法  
	b, err := json.Marshal(*player)
	if err != nil {
		return err
	}

	resp, nil := client.Call("addplayer", string(b))
	if err == nil && resp.Code == "200" {
		return nil
	}
	return err
}

func (client *CenterClient) RemovePlayer(name string) error {
	//给CenterClient增加RemovePlayer方法
	ret, _ := client.Call("removeplayer", name)
	if ret.Code == "200" {
		return nil
	}
	return errors.New(ret.Code)
}

func (client *CenterClient) ListPlayer(params string) (ps []*Player, err error) {
	resp, _ := client.Call("listplayer", params)
	if resp.Code != "200" {
		err = errors.New(resp.Code)
		return
	}
	err = json.Unmarshal([]byte(resp.Body), &ps)
	return 
}

func (client *Centerclient) Broadcast(message string) error {

	m := &Message{Content:message}
	
	b, err := json.Marshal(m)
	if err != nil {
		return err
	}

	resp, _ := client.Call("broadcast", string(b))
	if resp.Code == "200" {
		return nil
	}
	return errors.New(resp.Code)
}


