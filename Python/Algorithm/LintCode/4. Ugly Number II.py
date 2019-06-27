class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    4. Ugly Number II
    Ugly number is a number that only have prime factors 2, 3 and 5.
    Design an algorithm to find the nth ugly number. 
    The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
    """
    def nthUglyNumber(self, n):
        # write your code here
        temp_array = []
        
        num = 1 
        
        n2 = 0
        n3 = 0
        n5 = 0
        
        temp_array.append(1)
        
        for i in range(n):
            # 循环n次
            # 求出初始为*2 *3 *5最小值
            # 然后判断出三者最小值 
            # 插入数组并向前移动索引， 但n3 n5索引还未移动，除非乘以对应值才会移动索引
            temp_min = min(temp_array[n2]*2, temp_array[n3]*3, temp_array[n5]*5)
            
            if temp_min >= 2 * temp_array[n2]:
                n2 += 1
            if temp_min >= 3 * temp_array[n3]:
                n3 += 1
            if temp_min >= 5 * temp_array[n5]:
                n5 += 1
            
            temp_array.append(temp_min)
            
        return temp_array[n-1]