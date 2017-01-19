class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            d = {}
            for i in points:
                dis = (p[0] - i[0]) ** 2 + (p[1] - i[1]) ** 2
                if str(dis) in d:
                    d[str(dis)] += 1
                else:
                    d[str(dis)] = 1
            for e in d:
                res += (d[e] * (d[e]-1))
        return res