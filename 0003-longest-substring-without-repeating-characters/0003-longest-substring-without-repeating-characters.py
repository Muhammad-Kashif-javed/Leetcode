class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        i = 0  # i = left  j = right
        max_len = 0
        dic = {}
        for j , v  in enumerate(s):
            if v in dic and i<=dic[v]:
                i = dic[v] + 1
            dic[v] = j  # Always update the character's latest index  
            
            max_len = max(max_len, j-i+1) # calculate length of window
        return max_len


        #Time Complexity: O(n)
        #Space Complexity O(n)