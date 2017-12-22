'''
744. Sum of first K even-length Palindrome numbers 



Given a integer k, find the sum of first k even-length palindrome numbers.
Even length here refers to the number of digits of a number is even.


Given k = 3, return 66 // 11 + 22 + 33 = 66 (Sum of first three even-length palindrome 
numbers)

Given k = 10, return 1496
// 11 + 22 + 33 + 44 + 55 + 66 + 77 + 88 + 99 + 1001 = 1496

'''
		  
class Solution:
    """
    @param k: 
    @return: the sum of first k even-length palindrome numbers
    """
    def sumKEven(self, k):
        # Write your code here
        result = 0 
        for i in range(1, k+1):
            i = str(i)
            i += i[::-1]
            i = int(i)
            result += i
	return result

