#59. 3Sum Closest 

#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

#Example
#For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if not numbers or len(numbers) < 3:
            return False
        if len(numbers) == 3:
            return numbers[0] + numbers[1] + numbers[2]
        
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[j], numbers[i] = numbers[i], numbers[j]
                    
        for i in range(len(numbers)-1):
            find_num = 
        return result

                    
                
                
