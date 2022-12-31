class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def searchNeedle(i,needle):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    return False
            return True
        for i in range(0,len(haystack)-len(needle)+1):
            if searchNeedle(i,needle):
                return i
        return -1
        # time complexity of the above solution is O(n*m) where n is number of strings and m is the length of the longest string 
        # if needle == "": return 0
        # lps = [0] * len(needle)
        # # we build lps array ===> longest prefix that is also a suffix and note that the prefix cannot be the entire string itself so but 0 in the first index of the array 
        # # time complexity is : O(m+n)
        # prevLPS, i = 0, 1
        # while i < len(needle):
        #     if needle[i] == needle[prevLPS]:
        #         lps[i] = prevLPS + 1
        #         prevLPS += 1
        #         i += 1
        #     elif prevLPS == 0:
        #         lps[i] = 0
        #         i += 1
        #     else:
        #         prevLPS = lps[prevLPS - 1]
        
        # i = 0 # ptr for haystack
        # j = 0 # ptr for needle
        # while i < len(haystack):
        #     if haystack[i] == needle[j]:
        #         i, j = i + 1, j + 1
        #     else:
        #         if j == 0:
        #             i += 1
        #         else:
        #             j = lps[j - 1]
        #     if j == len(needle):
        #         return i - len(needle)
        # return -1