class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        res=[]
        for word in strs:
            hashmap[''.join(sorted(word))].append(word) # sorted returns a list of sorted characters
        for item in hashmap:
            res.append(hashmap[item])
        return res