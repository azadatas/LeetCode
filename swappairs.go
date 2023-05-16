func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{Val: 0, Next: head}
	prev := dummy

	for head != nil && head.Next != nil {
		// Nodes to be swapped
		firstNode := head
		secondNode := head.Next

		// Swapping
		prev.Next = secondNode
		firstNode.Next = secondNode.Next
		secondNode.Next = firstNode

		// Reinitializing the pointers
		prev = firstNode
		head = firstNode.Next
	}

	return dummy.Next
}