package mp

import ("fmt")

type Player interface {
	Play(source string)
}

func Play(source, mtype string) {
	var p Player
	
	switch mtype {
		case "MP3":
			p = &MP3Player{}		
		//case "Wav":
		//	p = &WAVPlayer{}
		default:
			fmt.Println("Unsuppored music type", mtype)
			return 
	}

	p.Play(source)

}
