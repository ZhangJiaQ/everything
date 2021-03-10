package tree

func flatten(root *TreeNode)  {
	if root == nil {
		return
	}
	flatten(root.Left)
	flatten(root.Right)

	// 先存起来当前左右子树
	left := root.Left
	right := root.Right

	// 绑定右子树
	root.Left = nil
	root.Right = left

	// 将原先的右子树绑定到左子树末尾
	p := root
	for p.Right != nil {
		p = p.Right
	}
	p.Right = right

}