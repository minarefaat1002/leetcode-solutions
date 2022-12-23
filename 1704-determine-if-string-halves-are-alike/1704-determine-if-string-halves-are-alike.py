class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a,b=s[:n//2],s[n//2:]
        vowels = "aeiouAEIOU"
        count1 = 0
        count2 = 0
        for char in s[:len(s)//2]:
            if char in vowels:
                count1+=1
        for char in s[len(s)//2:]:
            if char in vowels:
                count2+=1
        return count1==count2