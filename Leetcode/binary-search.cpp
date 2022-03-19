// Binary Search
// https://leetcode.com/problems/binary-search/submissions/
// Easy, 18/03/2022
// Tailai Wang

#include <vector>
class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int r = nums.size() - 1;
        int l = 0;
        while (l <= r){
            int mid = (l + r) / 2;
            if (nums[mid] == target){
                return mid;
            }
            if (nums[mid] > target){
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }
};