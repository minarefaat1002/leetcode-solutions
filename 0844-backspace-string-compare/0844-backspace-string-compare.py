class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si, ti = len(s) - 1, len(t) - 1
        count_s = count_t = 0
        
        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if s[si] == '#':
                    count_s += 1
                    si -= 1
                elif s[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break
            
            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if t[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif t[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break
            
            
            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a" 
                return False
            if (ti >= 0 and si >= 0) and s[si] != t[ti]:
                return False
            
            si -= 1
            ti -= 1
        return True