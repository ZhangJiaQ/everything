package nsum

import (
	"sort"
)


func threeSum() {

}



func _twoSum(nums []int, target int) [][]int {

	// 实际不是leetcode题目版本，而是求出两个数之和并输出两个数字

	res := make([][]int, 0)
	sort.Ints(nums)
	left := 0
	right := len(nums) - 1


	for left < right {
		sum := nums[left] + nums[right]
		_left, _right := nums[left], nums[right]
		if sum == target {
			res = append(res, []int{nums[left], nums[right]})
			for left < right && nums[left] == _left {
				left++
			}
			for left < right && nums[right] == _right {
				right--
			}
		} else if sum < target {
			for left < right && nums[left] == _left {
				left++
			}
		} else {
			for left < right && nums[right] == _right {
				right--
			}
		}

	}
	return res
}
