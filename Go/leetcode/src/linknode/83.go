package linknode
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {

	if head == nil || head.Next == nil {
		return head
	}

	first := head
	next := head.Next

	for next != nil {
		if first.Val == next.Val {
			// delete Node
			first.Next = next.Next
			next.Next = nil
			next = first.Next
		} else {
			first = first.Next
			next = next.Next
		}
	}
	return head
}
