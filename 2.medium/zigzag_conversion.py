# https://leetcode.com/problems/zigzag-conversion/

class Solution:

    """
    Runtime 7 ms Beats 89.40%
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        i, d = 0, 1
        arr = [[] for _ in range(numRows)]

        for c in s:
            arr[i].append(c)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        return "".join(["".join(t) for t in arr])

    """
    Runtime 282 ms Beats 6.75%
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        temp = []
        cnt = 0
        
        for i, c in enumerate(s):
            if 0 < cnt <= numRows - 2:
                ta = ["-" for _ in range(numRows)]
                ta[numRows - cnt - 1] = c
                arr.append(ta)
                if cnt == numRows - 2:
                    cnt = 0
                    continue
                cnt += 1
                continue

            if len(temp) <= numRows:
                temp.append(c)
                if len(temp) == numRows:
                    arr.append(temp[:])
                    temp = []
                    cnt += 1
        if temp:
            while len(temp) < numRows:
                temp.append('-')
            arr.append(temp)

        answer = ""
        for i in range(numRows):
            for j in range(len(arr)):
                t = arr[j][i]
                if t == "-":
                    continue
                answer += t
        return answer
