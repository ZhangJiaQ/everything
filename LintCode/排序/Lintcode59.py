#59. 3Sum Closest 

#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

#Example
#For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#解题思路： 先进行冒泡排序 O(n^2)其实可以用内置sort进行快速排序O（log 2 N）
#	   再对排序好的数组进行遍历 设置一个指针为i 对数组进行遍历一次
#	   设置left right 在数组进行遍历时进行夹逼操作，当left<right时进行循环，
#	   求出sum与target，并记录在minclosed，如果新的差距比旧的小，改变minclosed与result的值
#	   如果sum比target大则right指针减一 小，则left指针加一
#	   最后通过紧逼法求出差距最小值   该算法时间复杂度为O(n2)+ O(n2) =O（n2）
#	   其实可以优化为O(log 2 n) + O(n2) ，将排序算法变为快速排序即可


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        minclosed = 1000000
        result = 0
        if not numbers or len(numbers) < 3:
            return False
        if len(numbers) == 3:
            return numbers[0] + numbers[1] + numbers[2]
        
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[j], numbers[i] = numbers[i], numbers[j]
                    
        for i in range(len(numbers)-2):
            left = i+1
            right = len(numbers) - 1
            while left<right:
                sum = numbers[i] + numbers[left] + numbers[right]
                diff = abs(sum - target)
                if diff < minclosed:
                    minclosed = diff
                    result = sum
                if sum == target:
                    return result
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return result
        
                
