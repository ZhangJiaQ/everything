package nsum

const INT_MAX = int(^uint(0) >> 1)
const INT_MIN = ^INT_MAX




func find132pattern(nums []int) bool {
	if len(nums) < 3{
		return false
	}
	stack := make([]int, 0)

	length := len(nums) - 1
	s2 := INT_MIN
	for 0 > length  {
		cur := nums[length]

		if cur < s2 {
			return true
		} else {
			for len(stack) > 0 && stack[0] > s2 {

			}

		}
		length--
	}
	return false

}