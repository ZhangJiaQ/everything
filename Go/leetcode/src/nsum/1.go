package nsum

import (
	"sort"
)

func twoSum(nums []int, target int) []int {

	indexMap := make(map[int]int)

	for index, value := range nums {
		indexMap[value] = index
	}

	sort.Ints(nums)
	left := 0
	right := len(nums) - 1



	for left < right {
		temp := nums[left] + nums[right]
		if temp == target{
			return []int{indexMap[nums[left]], indexMap[nums[right]]}
		} else if temp > target {
			right -= 1
		} else {
			left += 1

		}
	}
	return []int{0, 0}
}
