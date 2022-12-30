class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ")
        arr = []
        count = 0
        for word in words:
            arr.append([len(word),count,word.lower()])
            count += 1
        res = sorted(arr, key = lambda x: (x[0], x[1]))
        res[0][2] = res[0][2][0].upper() + res[0][2][1:]
        ans = ""
        for i,ele in enumerate(res):
            ans += ele[2] + (" "  if i < len(res)-1 else "")
        return ans