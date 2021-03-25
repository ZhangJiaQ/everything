package linknode

type ListNode struct {

		Val int
		Next *ListNode
//111
}



func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}


	firstHead := &ListNode{Val: 0, Next: head}

	first := firstHead
	next := firstHead.Next

	for next != nil {
		if next.Next != nil && next.Next.Val == next.Val {
			delVal := next.Val
			for next != nil && next.Val == delVal {
				// 移除所有有重复的数字
				first.Next = next.Next
				next.Next = nil
				next = first.Next
			}
		} else {
			first = first.Next
			next = next.Next
		}

	}
	return firstHead.Next

}
