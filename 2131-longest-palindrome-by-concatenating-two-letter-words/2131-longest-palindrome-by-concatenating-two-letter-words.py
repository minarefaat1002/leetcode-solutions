class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        Max = 0
        middle = ""
        for item in count:
            if item[0] == item[1] and count[item] > Max and count[item]%2 == 1:
                Max = count[item]
                middle = item
        del count[middle]
        length = 0
        for item in count:
            if item[0] == item[1]:
                length += count[item]*2 if count[item] % 2 == 0 else (count[item]-1)*2
            else:
                if item[::-1] in count:
                    length += min(count[item],count[item[::-1]])*4
                    count[item] = 0
                    count[item[::-1]] = 0
        return Max*2 + length