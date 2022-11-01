class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        i=0
        if s.isspace():
            return True
        while i<len(s):
            if s[i].isalnum():
                string=string + s[i].lower()
            i+=1
        l=0
        r=len(string)-1
        while l<=r and string[l]==string[r]:
            l+=1
            r-=1
        if r <= l :
            return True
        else:
            return False 
        
            