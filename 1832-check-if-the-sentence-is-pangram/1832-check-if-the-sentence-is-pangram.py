class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        Set = set()
        for letter in sentence:
                Set.add(letter)
        return len(Set) == 26