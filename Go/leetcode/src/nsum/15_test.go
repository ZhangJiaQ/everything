package nsum

import (
	"fmt"
	"testing"
)


func Test15(t *testing.T) {

	nums := []int{-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6}
	result := threeSum(nums)
	fmt.Println(``)
	fmt.Println(result)
	fmt.Println(``)
}