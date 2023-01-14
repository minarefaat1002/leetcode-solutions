class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        rank = [1]*26
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        for c1,c2 in zip(s1,s2):
            union(ord(c1)-ord('a'),ord(c2)-ord('a'))
        hashMap = {}
        for i in range(26):
            if find(i) not in hashMap:
                hashMap[find(i)] = [i]
            else:
                hashMap[find(i)].append(i)
        for item in hashMap:
            Min = item
            for char in hashMap[item]:
                Min = Min if Min < char else char
            hashMap[item].append(Min)
        s = ""
        for char in baseStr:
            s += chr(hashMap[find(ord(char)-ord('a'))][-1]+ord('a'))
        return s