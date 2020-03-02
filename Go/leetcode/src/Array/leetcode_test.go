package Array

import (
	"testing"
	"fmt"
)

func TestArray(t *testing.T) {
	nums := make([][]int, 3)
	nums[0] = []int{1,2,3}
	nums[1] = []int{4,5,6}
	nums[2] = []int{7,8,9}
	rotate(nums)
	fmt.Println(``)
	fmt.Println(nums)
	fmt.Println(``)
}


