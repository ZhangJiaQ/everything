package Array

func generateMatrix(n int) [][]int {

	/*
	给一个n
	产生一个N * N的且顺时针旋转一次的数组
	*/
	// 构建一个N*N的数组
	result := make([][]int, n)
	index := 0
	for index < n {
		result[index] = make([]int, n)
		index++
	}
	// 往里填数字




	return result
}
