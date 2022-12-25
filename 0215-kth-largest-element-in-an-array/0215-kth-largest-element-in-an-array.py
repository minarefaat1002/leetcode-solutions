class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #average time complexity of quickSelect algo is O(N)
        k = len(nums)-k
        def quickSort(l,r):
            pivot , p = nums[r],l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]
            if p>k : return quickSort(l,p-1)
            elif p<k : return quickSort(p+1,r)
            else: return nums[p]
        return quickSort(0,len(nums)-1)