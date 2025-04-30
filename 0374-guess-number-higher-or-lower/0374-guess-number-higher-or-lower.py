# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l =1
        r= n
        while l<=r:
            mid = (l+r)//2
            Guess = guess(mid)
            if Guess == 1:  # num<pick
                l= mid+1
            elif Guess == -1:   #num>pick
                r = mid-1
            else:
                Guess == 0   #num==pick
                return mid

                #Time complexiety O(log(n))
                #space complexiety O(1)


        