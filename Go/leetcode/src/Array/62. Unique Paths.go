package Array

import "fmt"

func uniquePaths(m int, n int) int {
	/*
	M*N的棋盘，每次可以选择向右或者向下走一步，求总共能多少种方案
	M=3 N=2  -> return 3
	m=7 n=3  -> return 28
	*/
	// 使用 深度优先遍历
	if m == 1 || n == 1 {
		return 1
	}
	result := 0
	bfsuniquePaths(&result, 1, 1, m, n)

	return result
}


func bfsuniquePaths(r *int,x, y,  m, n int) {
	fmt.Println(x, y)
	if x + 1 <= m && y + 1 <= n {
		*r++
		bfsuniquePaths(r, x+1, y, m, n)
		bfsuniquePaths(r, x, y + 1, m, n)
	} else if x + 1 <= m {
		*r++
		bfsuniquePaths(r, x+1, y, m, n)
	} else if y + 1 <= m {
		*r++
		bfsuniquePaths(r, x, y + 1, m, n)
	}
}