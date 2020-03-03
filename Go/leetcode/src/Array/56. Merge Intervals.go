package Array


func merge(intervals [][]int) [][]int {
	/*
	合并区间
	*/
	if len(intervals) == 1 {
		return intervals
	}

	result := make([][]int, 0)

	index := 1

	for index < len(intervals) {
		if intervals[index - 1][1] > intervals[index][0]{
			// 需要合并
			intervals[index][0] = intervals[index-1][0]
		}
	}

	index = 0
	for index < len(intervals) - 1 {
		if intervals[index][0] != intervals[index + 1][0] {
			result = append(result, intervals[index])
		}
	}
	return result

}
