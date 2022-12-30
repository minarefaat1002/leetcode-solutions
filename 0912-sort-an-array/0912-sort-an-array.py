class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) == 1:
                return 
            mid = len(arr)//2
            arr1 = arr[:mid]
            arr2 = arr[mid:]
            mergeSort(arr1)
            mergeSort(arr2)
            i = 0
            k = 0
            z = 0
            while k < len(arr1) and z < len(arr2):
                if arr1[k] < arr2[z]:
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
        mergeSort(nums)
        return nums
                
            