package nsum

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {

	result := make([][]int, 0)
	sort.Ints(nums)

	for i, v := range nums{
		if i > 0 {
			if v == nums[i-1] {
				continue
			}
		}
		target := 0 - v
		temp := _twoSum(&nums, target, i)
		for _i, _v :=range temp {
			if _i > 0 {
				if temp[_i][0] == temp[_i-1][0]{
					continue
				}
			}
			result = append(result, []int{v, _v[0], _v[1]})
		}

	}
	return result
}


func _twoSum(nums *[]int, target int, start int) [][]int {

	left := start + 1
	right := len(*nums) - 1
	fmt.Println(left, right)

	res := make([][]int, 0)


	for left < right {
		sum := (*nums)[left] + (*nums)[right]
		if sum == target {
			res = append(res, []int{(*nums)[left], (*nums)[right]})
			left ++
			right --
		} else if sum < target {
			left ++
		} else {
			right--
		}

	}
	return res
}
