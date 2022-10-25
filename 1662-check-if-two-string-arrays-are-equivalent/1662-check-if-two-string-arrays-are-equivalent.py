class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Str1 = ""
        # Str2 = ""
        # for word in word1:
        #     Str1+=word
        # for word in word2:
        #     Str2+=word
        # return Str1==Str2
        i=0
        j = 0
        x = 0
        y = 0
        maxLen = max(len(word1),len(word2))
        while i<len(word1) or j<len(word2):
            if i < len(word1):
                word11 = word1[i]
            if j<len(word2):
                word22 = word2[j]
            while x<len(word11) and y<len(word22):
                if word11[x]!=word22[y]:
                    return False
                else:
                    x+=1
                    y+=1
            if x==len(word11):
                x=0
                i+=1
            if y==len(word22):
                y=0
                j+=1
            
        return True