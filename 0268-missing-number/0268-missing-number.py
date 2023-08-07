class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res =len(nums) 
        for i in range(len(nums)):
            res += (i-nums[i])
        return res
        
        '''
        for O(1) memory we use XOR(^)
        2^3 ===>  10
                  11
                -------
                  01
if both bits are different the result is 1 otherwise zero
 (5^5)  ====> 101
              101
             ------
              000
 (5^5^3)====> 5^5 is zero then 0^3 is 3 
 note: zero ^ any number = the original number
 XOR is associative meaning that we can rearrange its terms [order doesn't matter]
 [0,1,2,3]^[0,1,3]  = 2
 time complexity for this solution is O(2n)
 another solution 
 Sum([0,1,2,3]) - sum([3,0,1]) =2 
 taking the sum of the array will take n so the time complexity is O(2n)
 we can calculate the sum of the array in O(1) using n(n+1)/2    (gauss's formula)
 
        '''