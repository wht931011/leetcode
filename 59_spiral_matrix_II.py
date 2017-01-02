class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        res = [[] for i in range(n)]
        for r in res:
            for i in range(n):
                r.append(0)
        num = [x+1 for x in range(n*n)]
        s1 = 0
        f1 = 0
        f2 = n
        e1 = n
        size = n * n
        i = 0
        while i != size:
            for n in range(s1,e1):
                if i == size: break
                res[f1][n] = num[i]
                i+=1
            for n in range(f1+1,f2):
                if i == size: break
                res[n][e1-1] = num[i]
                i+=1
            for n in range(e1-1-1,s1-1,-1):
                if i == size: break
                res[f2-1][n] = num[i]
                i+=1
            for n in range(f2-1-1,f1,-1):
                if i == size: break
                res[n][s1] = num[i]
                i+=1
            s1 +=1
            f1 +=1
            f2 -=1
            e1 -=1
        return res