class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        for i in digits:
            if len(res) == 0:
                for m in map[int(i)]:
                    tmp = m
                    res.append(tmp)
            else:
                tmp_res = []
                for m in map[int(i)]:
                    for s in res:
                        tmp = s + m
                        tmp_res.append(tmp)
                res = tmp_res
        return res