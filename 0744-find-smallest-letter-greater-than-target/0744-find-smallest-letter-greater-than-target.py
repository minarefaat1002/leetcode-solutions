class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for letter in letters:
        #     if letter > target:
        #         return letter
        # return letters[0]
        l = 0 
        r = len(letters) - 1
        while l<=r:
            mid = (l+r)//2
            if letters[mid] <= target:
                l = mid + 1
            elif letters[mid] > target:
                r = mid - 1
        return letters[l] if l!=len(letters) else letters[0]