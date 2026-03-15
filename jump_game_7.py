"""class Solution:#brute force
    maxi=0
    def recurse(self,s:str,minJump:int,maxJump:int,n:int,index:int)->bool:
        if  index>=n:
            return 0
        if s[index]=='0' and index==n-1:
            return 1
        for j in range(maxJump,minJump-1,-1):
            if index+j<n and s[index+j]=='0':
                maxi=max(Solution.maxi,self.recurse(self,s=s,minJump=minJump,maxJump=maxJump,n=n,index=index+j))
        return maxi

        
    def canReach(self, s: str, minJump: int, maxJump: int)-> bool:
        n=len(s)
        if s[n-1]=='1':#edge case
            return False
        a=self.recurse(self,s=s,minJump=minJump,maxJump=maxJump,n=n,index=0)
        if a==1:
            return True
        return False"""

class Solution:#dynamic programming
    
    def recurse(self,s:str,minJump:int,maxJump:int,n:int,index:int,dp:list)->bool:
        maxi=0
        if  index>=n:
            return 0
        if dp[index] !=-1:
            print(index)
            return dp[index]
        if s[index]=='0' and index==n-1:
            dp[index]=1
            return 1
        for j in range(maxJump,minJump-1,-1):
            if index+j<n and s[index+j]=='0':
                maxi=max(maxi,self.recurse(self,s=s,minJump=minJump,maxJump=maxJump,n=n,index=index+j,dp=dp))
        dp[index]=maxi
        return dp[index]
    def canReach(self, s: str, minJump: int, maxJump: int)-> bool:
        n=len(s)
        if s[n-1]=='1':#edge case
            return False
        dp=[-1]*n
        a=self.recurse(self,s=s,minJump=minJump,maxJump=maxJump,n=n,index=0,dp=dp)
        if a==1:
            return True
        return False





from collections import deque 
class Solution: 
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool: #apply BFS 
        n=len(s) 
        if s[n-1]=='1':#edge case 
            return False 
        l=[0]*n 
        for i in range(0,n): l[i]=s[i] i=0 
        # print(n) 
        q=deque() 
        while True: 
            c=0 
            for j in range(maxJump,minJump-1,-1): 
                if i+j==n-1 and l[i+j]!='1': 
                    return True 
                elif i+j<n and l[i+j]!='1': 
                    # print(i+j) 
                    c=c+1 
                    if l[i+j]=='0': 
                        q.append(i+j) 
                        l[i+j]='2'#mark as visited 
            if c==0 and (len(q)==0):#from current i, i can't move to any right places 
                return False 
            i=q.popleft() 
            # print(i) 
        return False
    

from collections import deque#optimal bfs
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1':
            return False
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            start = max(i + minJump, farthest)#optimized BFS
            end = min(i + maxJump + 1, n)# to prevent out of bound erros
            for j in range(start, end):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    q.append(j)
            farthest = end
        return False


        

    

if __name__=="__main__":
    s=Solution
    string="011010011001100000111111110"
    a=s.canReach(s,string,minJump=2,maxJump=5)
    print(a)
    


    
