class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            for number in word.split(separator):
                if number:
                    result.append(number)
        return result