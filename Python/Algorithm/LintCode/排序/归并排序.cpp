#include <iostream>
#include <vector>
#include <string>
#include<iterator>
#include<limits.h>

using std::vector;
using std::string;
using std::cin;
using std::cout;
using std::endl;


void Merge(vector<int> &A, int p, int q, int r) {
	int n1 = q - p + 1;
	int n2 = r - q + 1;
	// 声明两个vector用来存储排序好的数列
	vector<int> left(n1 + 1, 0), right(n2, 0);
	for (int i = 0; i < n1; ++i) {
		left[i] = A[p + i];
	}
	left[n1] = 2147483647;
	for (int j = 0; j < n2 - 1; ++j) {
		right[j] = A[q + j + 1];
	}
	right[n2 - 1] = 2147483647;
	int i = 0, j = 0;
	for (int k = p; k < r + 1; ++k) {
		if (left[i] > right[j]) {
			A[k] = right[j];
			++j;
		}
		else {
			A[k] = left[i];
			++i;
		}
	}

}

void MergeSort(vector<int> &A, int p, int r) {
	if (p < r) {
		int q = (p + r) / 2;
		MergeSort(A, p, q);
		MergeSort(A, q + 1, r);
		Merge(A, p, q, r);
	}
}




int main() {
	// 定义一个ector

	vector<int> unSortArray = { 2,4,5,7,1,2,3,6 };
	MergeSort(unSortArray, 0, unSortArray.size() - 1);



	for (auto a : unSortArray) {
		cout << a;
	}
	system("pause");
	return 1;
}