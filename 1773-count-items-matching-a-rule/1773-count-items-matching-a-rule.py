class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0 
        hashMap = {"type":0,"color":1,"name":2}
        for item in items:
            index = hashMap[ruleKey]
            count += 1 if item[index] == ruleValue else 0
        return count 