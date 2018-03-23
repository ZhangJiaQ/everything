#Sort Letters by Case 

#Given a string which contains only letters. Sort it by lower case first and upper case second.

#Example
#For "abAcD", a reasonable answer is "acbAD"Example
#For "abAcD", a reasonable answer is "acbAD"


class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here

        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                num1 = 0
                num2 = 0
                num1 = ord(chars[i])+200 if ord(chars[i]) <97 else ord(chars[i])
                num2 = ord(chars[j])+200 if ord(chars[j]) <97 else ord(chars[j])
                if num2 < num1:
                    chars[i], chars[j] = chars[j], chars[i]
                    
        return chars
