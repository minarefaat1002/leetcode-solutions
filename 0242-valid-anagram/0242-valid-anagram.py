class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True
        # time complexity = O(nlogn) ===> where n is the length of either string
        if len(s)!=len(t):
            return False
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char,0)+1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char]-=1
            if hashmap[char] == 0:
                del hashmap[char]
        return True