class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n>>1
        return res
    # it will take O(32)
    # >>1  right shift by 1
    '''
    while n:
        n = n&(n-1)
        res+=1
    return res
    '''
    '''
    each time we and n with n-1 we get rid of the right most set bit 
    ex : 1000001 ==> stubract 1 from it  ==> 1000000
    ex: 1000000 ==> subtract 1 from it ===> 0111111 ==> note that we get rid of the right most set bit but there are many set bits appears at the right of our bit . but no problem because these bits will be removed when we and them in the next time 
    '''