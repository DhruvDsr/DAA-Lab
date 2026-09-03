//Program 2: Allocate Minimum Pages

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;
bool isValid(vector<int>& arr, int m, int mid) {
 int students = 1, currentSum = 0;
 for (int pages : arr) {
 if (currentSum + pages > mid) {
 students++;
 currentSum = pages;
 if (students > m) return false;
 } else {
 currentSum += pages;
 }
 }
 return true;
}
int findPages(vector<int>& arr, int m) {
 if (m > arr.size()) return -1;
 int low = *max_element(arr.begin(), arr.end());
 int high = accumulate(arr.begin(), arr.end(), 0);
 int res = -1;
 while (low <= high) {
 int mid = low + (high - low) / 2;
 if (isValid(arr, m, mid)) {
 res = mid; high = mid - 1;
 } else {
 low = mid + 1;
 }
 }
 return res;
}
int main() { return 0; }