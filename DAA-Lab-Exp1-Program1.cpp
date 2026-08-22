//Program 1: Insertion Sort (Iterative and Recursive)

#include <iostream>
#include <vector>

using namespace std;

void insertionSortIterative(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void insertionSortRecursive(vector<int>& arr, int n) {
    if (n <= 1) return;

    
    insertionSortRecursive(arr, n - 1);

    
    int last = arr[n - 1];
    int j = n - 2;

    while (j >= 0 && arr[j] > last) {
        arr[j + 1] = arr[j];
        j = j - 1;
    }
    arr[j + 1] = last;
}

int main() {
    vector<int> arr1 = {8, 4, 2, 9, 5};
    vector<int> arr2 = {8, 4, 2, 9, 5};

    insertionSortIterative(arr1);
    cout << "Iterative Sort Output: ";
    for (int v : arr1) cout << v << " ";
    cout << endl;

    insertionSortRecursive(arr2, arr2.size());
    cout << "Recursive Sort Output: ";
    for (int v : arr2) cout << v << " ";
    cout << endl;

    return 0;
}