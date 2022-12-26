class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = {}
        hashmap2 ={}
        res = []
        for num in nums1:
            hashmap1[num]= hashmap1.get(num,0)+1
        for num in nums2:
            hashmap2[num] = hashmap2.get(num,0)+1
        for item in hashmap1:
            if item in hashmap2:
                for i in range(min(hashmap1[item],hashmap2[item])):
                    res.append(item)
        return res 
    