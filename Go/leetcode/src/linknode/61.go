package linknode

func rotateRight(head *ListNode, k int) *ListNode {

	if head == nil {
		return head
	}


	length := 1
	tail := head
	for tail.Next != nil {
		length += 1
		tail = tail.Next
	}

	tail.Next = head

	k = length - k % length

	first := head

	for k > 1 {
		first = first.Next
		k -= 1
	}

	head = first.Next
	first.Next = nil

	return head


}