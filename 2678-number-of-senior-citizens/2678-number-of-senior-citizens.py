class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            count+= 1 if detail[11:13] > '60' else 0
        return count 