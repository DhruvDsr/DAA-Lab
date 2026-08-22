// Program 3: Majority Element

#include <iostream>
#include <vector>

using namespace std;

int majorityElement(vector<int>& arr) {
    int candidate = -1;
    int count = 0;
    int n = arr.size();

    for (int i = 0; i < n; i++) {
        if (count == 0) {
            candidate = arr[i];
            count = 1;
        } 
        else if (arr[i] == candidate) {
            count++;
        } 
        else {
            count--;
        }
    }

    int verify_count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == candidate) {
            verify_count++;
        }
    }

    if (verify_count > n / 2) {
        return candidate;
    }
    
    return -1; 
}

int main() {
    vector<int> arr = {2, 2, 1, 2, 3, 2, 2};
    
    int result = majorityElement(arr);
    
    if (result != -1) {
        cout << "Majority Element is: " << result << endl;
    } else {
        cout << "No Majority Element found." << endl;
    }

    return 0;
}