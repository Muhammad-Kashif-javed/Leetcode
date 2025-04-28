class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        num = x
        revnum = 0
        while num>0:
            last_digit = num%10
            revnum = revnum * 10 + last_digit
            num=num//10
        if revnum==x:
            return True
        else:
            return False
            
'''Time Complexity:

The key operation happens inside the while num > 0: loop.
In each iteration, you divide num by 10 (num = num // 10).
Therefore, the number of iterations is proportional to the number of digits in x.
The number of digits in a number x is approximately log₁₀(x).
(Because if x has d digits, then 10^(d-1) <= x < 10^d.)
Thus, the time complexity is:𝑂(log10(𝑥)) or O(log(x))
​Space Complexity:
You use a few integer variables (num, revnum, last_digit), but no extra space that grows with input size.
Thus, space complexity is: 𝑂(1)'''

​

