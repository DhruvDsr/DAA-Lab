// Program 2: Dutch National Flag Problem

#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

void dutchNationalFlag(vector<int>& arr) {
    int low = 0;
    int mid = 0;
    int high = arr.size() - 1;

    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } 
        else if (arr[mid] == 1) {
            mid++;
        } 
        else { 
            swap(arr[mid], arr[high]);
            high--;
        }
    }
}

int main() {
    vector<int> arr = {2, 0, 1, 2, 1, 0, 0};
    
    dutchNationalFlag(arr);
    
    cout << "Sorted Array: ";
    for (int v : arr) cout << v << " ";
    cout << endl;

    return 0;
}
