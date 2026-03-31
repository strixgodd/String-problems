class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=""
        l=len(s)
        if numRows==1:
            for i in range(l):
                ans+=s[i]
            return ans

        matrix=[[] for _ in range(numRows)]
        j=0#signifies the row no.
        step=1
        for i in range(l):
            matrix[j].append(s[i])
            j+=step
            if j==0 or j==numRows-1:
                step*=-1
        for i in range(numRows):
            size=len(matrix[i])
            for j in range(size):
                ans+=matrix[i][j]
        return ans
            

