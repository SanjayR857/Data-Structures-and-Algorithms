/**
 * Merge Sort in C++ (C++17)
 * 
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */

#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    // TODO: Allocate temporary vector or copy subarrays
    // TODO: Compare elements from left and right subarrays and merge
    // TODO: Copy merged elements back to arr[left..right]
}

void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    // TODO: Recursively sort left and right halves
    // merge_sort(arr, left, mid);
    // merge_sort(arr, mid + 1, right);
    // merge(arr, left, mid, right);
}

int main() {
    std::vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    // merge_sort(arr, 0, arr.size() - 1);
    return 0;
}
