class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # items = [[0]*26 for _ in range(26)]
        # for vote in votes:
        #     for i in range(len(vote)):
        #         items[ord(vote[i]) - ord('A')][i] += 1
        # for i in range(26):
        #     items[i].append(25-i)
        #     items[i].append(chr(ord('A')+i))
        # items.sort(reverse = True)
        # res = ""
        # for item in items:
        #     res += item[-1] if item[-1] in votes[0] else ""
        # return res
        d = {}
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1

        voted_names = sorted(d.keys()) # sorting by key
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))