class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indexed_nums = [(nums[key_index], key_index) for key_index in range(len(nums))]
        def mergeSort(arr):
            if len(arr) < 2:
                return 
            mid = len(arr)//2
            arr1 = arr[:mid]
            mergeSort(arr1)
            arr2 = arr[mid:]
            mergeSort(arr2)
            i = 0
            k = 0
            z = 0
            while k < len(arr1) and z < len(arr2):
                if arr1[k][0] > arr2[z][0]:
                    counts[arr1[k][1]] += len(arr2) - z
                    arr[i] = arr1[k]
                    k+=1
                    i+=1
                else:
                    arr[i] = arr2[z]
                    z+=1
                    i+=1
            while k < len(arr1):
                arr[i] = arr1[k]
                k+=1
                i+=1
            while z < len(arr2):
                arr[i] = arr2[z]
                z+=1
                i+=1
        mergeSort(indexed_nums)
        return counts
                
            