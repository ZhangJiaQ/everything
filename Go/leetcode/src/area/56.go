package Area

import (
	"fmt"
	"sort"
)

func merge(intervals [][]int) [][]int {

	sort.Slice(intervals, func(a, b int) bool {
		if intervals[a][0] != intervals[b][0] {
			return intervals[a][0] - intervals[b][0] < 0
		} else {
			return intervals[a][1] - intervals[b][1] > 0
		}
	})

	result := make([][]int, 0)

	left := intervals[0][0]
	right := intervals[0][1]

	for i:=1; i<len(intervals) ; i++ {
		if intervals[i][0] <= right {
			// xiangjiao
			intervals[i][0] = left
			if intervals[i][1] >= right {
				right = intervals[i][1]
			} else {
				intervals[i][1] = right
			}
		}  else {
			// not xiangjiao
			result = append(result, intervals[i - 1])
			left = intervals[i][0]
			right = intervals[i][1]
		}
		fmt.Println(left, right, result, i , intervals)
	}
	result = append(result, intervals[len(intervals) - 1])


	return result
}