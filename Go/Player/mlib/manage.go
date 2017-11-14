package library

import ("errors")

type MusicEntry struct {
    Id string
    Name string
    Artist string
    Genre string
    Source string
    Type string
}

type MusicManager struct {
    musics []MusicEntry
}

func NewMusicManager() *MusicManager {       //给MusicManager对象增加NewMusicManager方法
    return &MusicManager{make([]MusicEntry, 0)}
}

func (m *MusicManager) Len() int {      //给MusicManager对象增加len方法
    return len(m.musics) 
}

func (m *MusicManager) Get(index int) (music *MusicEntry, err error){
    //给MusicManager对象增加get方法
    if index < 0 || index >= len(m.musics){
        return nil, errors.New("Index out of range.")    
    }
    return &m.musics[index], nil
}

func (m *MusicManager) Find(name string) *MusicEntry{
     //给MusicManager对象增加Find方法
    if len(m.musics) == 0 {
        return nil    
    }
    
    for _, m := range m.musics {
        if m.Name == name {
            return &m        
        }    
    }
    return nil
}

func (m *MusicManager) Add (music *MusicEntry) {
    //给MusicManager对象增加Add方法
    m.musics = append(m.musics, *music)
}

func (m *MusicManager) Remove(index int) *MusicEntry {
    //给MusicManager对象增加Remove方法
    if index < 0 || index >= len(m.musics){
        return nil
    }

    removedMusic := &m.musics[index]

    //make remove
    if index < len(m.musics)-1 {
        m.musics = append(m.musics[:index-1], m.musics[index+1:]...)
    } else if index == 0 {
        m.musics = make([]MusicEntry, 0)
    } else {
        m.musics = m.musics[:index-1]
    }
    
    return removedMusic

}

func (m *MusicManager) RemoveByName(name string) *MusicEntry {
	var removedMusic *MusicEntry = nil
	var iPos int = -1
	for i := 0; i < m.Len(); i++ {
		if m.musics[i].Name == name {
			iPos = i
			break		
		}
	}
	if iPos < 0 {
		return nil
	}

	removedMusic = m.Remove(iPos)

	return removedMusic
}
