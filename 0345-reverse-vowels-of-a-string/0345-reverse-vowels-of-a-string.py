class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        l = 0 
        r = len(s)-1
        stack = []
        for char in s:
            stack.append(char)
        while l < r:
            if stack[l].lower() in vowels and stack[r].lower() in vowels:
                temp = stack[l]
                stack[l] = stack[r]
                stack[r] = temp
                l+=1
                r-=1
            elif stack[l].lower() in vowels:
                r-=1
            elif stack[r].lower() in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return "".join(stack)
            