package Array

import (
	"testing"
	"fmt"
)

func TestArray(t *testing.T) {
	nums := []int{0,1,0,2,1,0,1,3,2,1,2,1}

	data := trap(nums)
	fmt.Println(``)
	fmt.Println(data)
	fmt.Println(``)
	}


