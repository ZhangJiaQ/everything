'''
380. Intersection of Two Linked Lists 

Write a program to find the node at which the intersection of two singly linked lists begins.

'''


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        p1 = headA
        p2 = headB
        lenA = 0
        lenB = 0
        while p1:
            lenA += 1
            p1 = p1.next
            
        while p2:
        lenB +  = 1
        p2      = p2.next
            
        p1 = headA
        p2 = headB
        
        if lenA > lenB:
            len_num = lenA-lenB
            while len_num:
                p1 = p1.next
                len_num -= 1
            len_num = lenB
        else:
            len_num = lenB-lenA
            while len_num:
                p2 = p2.next
                len_num -= 1
            len_num = lenA
            
        while len_num:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next
            len_num -= 1
            
        return None
