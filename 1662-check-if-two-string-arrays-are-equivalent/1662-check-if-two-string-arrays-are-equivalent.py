class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Str1 = ""
        Str2 = ""
        for word in word1:
            Str1+=word
        for word in word2:
            Str2+=word
        return Str1==Str2