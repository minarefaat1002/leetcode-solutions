# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n = rand7() + (rand7()-1)*7
        while n > 40:
            n = rand7() + (rand7()-1)*7
        return n%10 + 1