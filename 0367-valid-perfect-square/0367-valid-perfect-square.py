class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l<=r:
            mid = (l+r)//2
            if mid*mid == num:
                return True 
            elif mid*mid > num:
                r=mid-1
            else:
                l=mid+1
        return False
        
        '''
        for i in range(1,int(num/2 +1),1):
            if i*i ==num:
                return True
        return False
        '''