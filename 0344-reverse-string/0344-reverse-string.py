class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right = len(s)-1
        left = 0 
        while left<=right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left +=1
            right -=1
        # def reverse(l,r):
        #     if l < r:
        #         s[l],s[r] = s[r],s[l]
        #         reverse(l+1,r-1)
        # reverse(0,len(s)-1)