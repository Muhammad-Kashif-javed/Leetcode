class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maximum = max(nums)  #O(n)
        index = nums.index(maximum) #O(n)
        return index
# TC O(n+n)= O(n)
#SC O(1)
        