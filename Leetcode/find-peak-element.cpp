// Find Peak Element
// https://leetcode.com/problems/find-peak-element/
// Medium (Algorithms II), 19/03/2022
// Tailai Wang

#include <vector>

class Solution {
public:
    int findPeakElement(std::vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;
        while (l < r){
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1]){
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};