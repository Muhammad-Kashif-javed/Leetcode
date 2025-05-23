class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr_sum = 0
        max_sum = 0
        freq = {}
        for i in range (k):
            if nums[i] in freq:
                freq[nums[i]]= freq[nums[i]] + 1
            else:
                freq[nums[i]] = 1
            curr_sum= curr_sum + nums[i]
        if len(freq) == k:
            max_sum = curr_sum
        for j in range(k,n):
            curr_sum = curr_sum + nums[j]
            curr_sum = curr_sum - nums[j-k]
            freq[nums[j-k]] = freq[nums[j-k]] -1
            if freq[nums[j-k]]==0:
                del freq[nums[j-k]]
            if nums[j] in freq:
                freq[nums[j]] = freq[nums[j]] +1
            else:
                freq[nums[j]] = 1
            
            if len(freq)==k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
          
#Time Complexity: O(n)

#Space Complexity: O(k)
                
    

        