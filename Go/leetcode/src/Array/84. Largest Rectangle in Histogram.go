package Array

import "fmt"

func largestRectangleArea(heights []int) int {
	/*
	Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
	*/

	// 给一个数组   上面写了Y坐标的高度
	// 求出X与Y坐标围成地最大面积
	//贪心就可以了     先左右最大地开始 然后慢慢向内围住 最后返回最大面积 完事儿

	if len(heights) < 1 {
		return 0
	}
	if len(heights) == 1 {
		return heights[0]
	}
	minCoordinateArray := make([][]int, 0)
	maxArea := 0
	left, right := 0, len(heights) - 1

	for left <= right {
		if len(minCoordinateArray) == 0 {
			// 需要找到目前区间内最小值
			FindMinNum(&heights, &minCoordinateArray, left, right)
		}
		tempArea := (right-left+1) * minCoordinateArray[0][1]
		if tempArea > maxArea {
			maxArea = tempArea
		}
		if heights[left] < heights[right] {
			if minCoordinateArray[0][1] == heights[left] {
				// remove
				RemoveNum(&minCoordinateArray, left)
			}
			left += 1
		} else {
			if minCoordinateArray[0][1] == heights[right] {
				// remove
				RemoveNum(&minCoordinateArray, right)
			}
			right -= 1
		}

	}
	return maxArea



}


func FindMinNum (number *[]int, minCoordinateArray *[][]int, start, end int){
	fmt.Println(start, end)
	*minCoordinateArray = append(*minCoordinateArray, []int{start, (*number)[start]})

	for index, value := range (*number)[start+1:end+1] {
		if value == (*minCoordinateArray)[0][1] {
			// 等于 加入
			*minCoordinateArray = append(*minCoordinateArray, []int{start+index, value})
		} else if value < (*minCoordinateArray)[0][1] {
			// 小于的话 清空数组，然后加入目前小于的这个值
			*minCoordinateArray = [][]int{}
			*minCoordinateArray = append(*minCoordinateArray, []int{start+index, value})
		}
	}
}

func RemoveNum(minCoordinateArray *[][]int, index int) {
	if len(*minCoordinateArray) == 1 {
		*minCoordinateArray = [][]int{}
		return
	}

	findIndex := 0
	for i, v:= range *minCoordinateArray {
		if v[0] == index {
			findIndex = i
			break
		}
	}
	*minCoordinateArray = append((*minCoordinateArray)[:findIndex], (*minCoordinateArray)[findIndex:]...)
}
