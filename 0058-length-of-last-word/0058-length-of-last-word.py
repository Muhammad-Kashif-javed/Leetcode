class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len = 0
        for i in s[::-1]:
            if i == " ":
                if len>=1:
                    break
            else:
                len+=1
        return len
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        