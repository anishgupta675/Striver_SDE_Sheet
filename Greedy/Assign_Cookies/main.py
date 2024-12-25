class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, res = 0, 0
        while i < len(s) and res < len(g):
            if s[i] >= g[res]:
                res += 1
            i += 1
        return res
