package Area

import (
	"fmt"
	"testing"
)

func TestArray(t *testing.T) {

	nums := [][]int{{1,5},{1,4},{3,6},{2,8}}
	result := removeCoveredIntervals(nums)
	fmt.Println(``)
	fmt.Println(result)
	fmt.Println(``)
}