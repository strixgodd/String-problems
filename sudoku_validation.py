class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check every row,every col, every 3x3 grid with a constant size array of size 9 (0..8)
        #check all rows
        n=len(board[0])
        for i in range(0,n):
            temp=[0]*(n+1)
            for j in range(0,n):
                ch=board[i][j]
                if ch!=".":
                    intval=ord(ch)-ord("0")
                    temp[intval]=temp[intval]+1
                    if temp[intval]>=2:
                        return False
        #check all cols
        for i in range(0,n):
            temp=[0]*(n+1)
            for j in range(0,n):
                ch=board[j][i]
                if ch!=".":
                    intval=ord(ch)-ord("0")
                    temp[intval]=temp[intval]+1
                    if temp[intval]>=2:
                        return False
        #check all 3x3 grids

        for k in range(0,9,3):
            for m in range(0,9,3):
                temp=[0]*(n+1)
                for i in range(k,k+3):
                    for j in range(m,m+3):
                        ch=board[i][j]
                        if ch!=".":
                            intval=ord(ch)-ord("0")
                            temp[intval]=temp[intval]+1
                            if temp[intval]>=2:
                                return False

        return True
                



#can also be solved using hashset instead of array of size 10.





        