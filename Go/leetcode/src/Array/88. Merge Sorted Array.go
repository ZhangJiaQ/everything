package Array

func merge(nums1 []int, m int, nums2 []int, n int)  {
	/*
	n, m两个数组
	*/

	left := 0
	right := 0
	for left < m {
		if nums1[left] == 0{
			break
		}
		if nums1[left] < nums2[right] {
			left += 1
		} else {
			// swap
			nums1[left], nums2[right] = nums2[right] ,nums1[left]
			left++
		}
	}


}
