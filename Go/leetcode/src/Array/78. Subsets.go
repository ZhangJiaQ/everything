package Array
func subsets(nums []int) [][]int {

	/*
	Given a set of distinct integers, nums, return all possible subsets (the power set)
	Note: The solution set must not contain duplicate subsets.
	*/
	result := make([][]int, 0)
	result = append(result, []int{})
	if len(nums) == 0 {
		return result
	}





	return result
}

