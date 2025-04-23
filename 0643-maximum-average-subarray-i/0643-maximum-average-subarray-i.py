class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum/k

        for j in range(k,n):
            curr_sum+=nums[j]
            curr_sum-=nums[j-k]
            avg = curr_sum/k
            max_avg = max(avg, max_avg)
        return max_avg

🕒 Time Complexity: O(n)
The first loop runs k times to calculate the sum of the first window. The second loop runs n - k times 
Total iterations: k + (n - k) = n. So, Time Complexity = O(n)

💾 Space Complexity: O(1)
You're only using a few variables: curr_sum, max_avg, and avg (temporary).No additional space is used proportional to input size.
So, Space Complexity = O(1)
