// Program 1: Union and Intersection of Two Sorted Arrays

#include <iostream>
#include <vector>
using namespace std;
void findUnionIntersection(vector<int>& arr1, vector<int>& arr2) {
int i = 0, j = 0;
vector<int> uni, inter;
while (i < arr1.size() && j < arr2.size()) {

if (arr1[i] < arr2[j]) {
uni.push_back(arr1[i++]);
} else if (arr2[j] < arr1[i]) {
uni.push_back(arr2[j++]);
} else {
uni.push_back(arr1[i]);
inter.push_back(arr1[i]);
i++; j++;
}
}
while (i < arr1.size()) uni.push_back(arr1[i++]);
while (j < arr2.size()) uni.push_back(arr2[j++]);
cout << "Union: ";
for (int v : uni) cout << v << " ";
cout << "\nIntersection: ";
for (int v : inter) cout << v << " ";
cout << endl;
}
int main() {
vector<int> A = {1, 2, 4, 5};
vector<int> B = {2, 4, 6};
findUnionIntersection(A, B);
return 0;
}