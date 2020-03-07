package Array

import (
	"testing"
	"fmt"
)

func TestArray(t *testing.T) {

	numbers := [][]byte{{'a', 'b','c','e'},{'s', 'f','c','s'},{'a', 'd','e','e'}}
	str := `abcced`
	result := exist(numbers, str)
	fmt.Println(``)
	fmt.Println(result)
	fmt.Println(``)
}


