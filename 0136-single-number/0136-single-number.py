class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            nums_set = set(nums)
            sum_set = sum(nums_set)
            sum_nums = sum(nums)
            result = 2 * sum_set - sum_nums
            return result
            
        #Time Complexity: O(n)
        #Space Complexity: O(1)
    
    # Step 1: Convert to set (removing duplicates)
    # Step 2: Calculate the sum of the set
    # Step 3: Calculate the sum of the original list
    # Step 4: Return the result
   
