class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numberOfOnes(num):
            counter = 0
            while num:
                counter += num%2
                num = num//2
            return counter
        return sorted(arr, key=lambda a: [numberOfOnes(a),a])
            