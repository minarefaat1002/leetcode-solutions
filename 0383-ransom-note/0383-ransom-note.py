class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        for char in count1:
            freq1 = count1[char]
            freq2 = count2[char]
            if freq1 > freq2:
                return False
        return True