# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l=0
        r=n-1
        result=0
        while l<=r:
            mid=(r+l)//2
            if isBadVersion(mid+1):
                result = mid+1
                r=mid-1
            else:
                l=mid+1
        return result 
        """
        :type n: int
        :rtype: int
        """
        