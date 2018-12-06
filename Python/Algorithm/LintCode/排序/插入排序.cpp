#include <iostream>
#include <vector>
#include <string>
#include<iterator>

using std::vector;
using std::string;
using std::cin;
using std::cout;
using std::endl;


int main() {
	// 定义一个ector

	vector<int> unSortArray = { 5,2,4,6,1,3 };
	for (int j = 1; j < unSortArray.size(); j++) {
		int key = unSortArray[j];
		int i = j - 1;
		while (i >= 0 && unSortArray[i] > key) {
			unSortArray[i + 1] = unSortArray[i];
			i -= 1;
		}
		unSortArray[i + 1] = key;
	}
	for (auto a : unSortArray) {
		cout << a;
	}
	system("pause");
	return 1;
}