package nsum

import (
	"fmt"
	"testing"
)

func Test1(t *testing.T) {

	nums := []int{1,2,3,2,3,3,4,5}
	result := twoSum(nums, 6)
	fmt.Println(``)
	fmt.Println(result)
	fmt.Println(``)
}