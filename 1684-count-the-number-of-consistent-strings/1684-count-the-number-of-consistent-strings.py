class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def wordIsConsistent(word):
            for char in word:
                if char not in allowed:
                    return False
            return True
        allowed = set(allowed)
        count = 0
        for word in words:
            if wordIsConsistent(word):
                count+=1
        return count