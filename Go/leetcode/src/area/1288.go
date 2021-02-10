package Area

import (
    "fmt"
    "sort"
)

func removeCoveredIntervals(intervals [][]int) int {
	/*
		Given a list of intervals, remove all intervals that are covered by another interval in the list.
		Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
		After doingX so, return the number of remaining intervals.
		Example 1:
		Input: intervals = [[1,4],[3,6],[2,8]]
		Output: 2
		Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
		Example 2:
		Input: intervals = [[1,4],[2,3]]
		Output: 1
		Example 3:
		Input: intervals = [[0,10],[5,12]]
		Output: 2
		Example 4:
		Input: intervals = [[3,10],[4,10],[5,11]]
		Output: 2
		Example 5:
		Input: intervals = [[1,2],[1,4],[3,4]]
		Output: 1
	*/
	//逻辑 先排序后处理
	sort.Slice(intervals, func(a, b int) bool {
		if intervals[a][0] != intervals[b][0] {
			return intervals[a][0] - intervals[b][0] < 0
		} else {
			return intervals[a][1] - intervals[b][1] > 0
		}
	})
	fmt.Print(intervals)
	result := 0
	firstLeft := intervals[0][0]
	firstRight := intervals[0][1]

	for i := 1; i < len(intervals); i++ {
		//找到覆盖区间
		if firstLeft <= intervals[i][0] && firstRight >= intervals[i][1] {
			result++
		}

		// 相交区间合并
		if firstRight >= intervals[i][0] && firstRight <= intervals[i][1] {
			firstRight = intervals[i][1]
		}
		//完全不包含
		if firstRight <= intervals[i][0] {
			firstRight = intervals[i][1]
			firstLeft = intervals[i][0]
		}

	}


	return len(intervals) - result
}
