class Solution:
    def countSort(self, arr: list) -> list: #SC=O(max val in arr) , TC= O(max val in arr)
        ans=[0]*len(arr)
        maximum=max(arr)
        cntArr=[0]*(maximum+1)
        for i in arr:
            cntArr[i]+=1
        #cumulative sum
        for i in range(1,len(cntArr)):
            cntArr[i]=cntArr[i]+cntArr[i-1]
            
        #final updation of ans array, traversing arr backwards for stable sorting
        for i in range(len(arr)-1,-1,-1):
            ans[cntArr[arr[i]]-1]=arr[i]
            cntArr[arr[i]]-=1

        return ans
        
    
if __name__=="__main__":
    sol=Solution()
    arr=[5,4,3,3,1]
    ans=sol.countSort(arr)
    for i in ans:
        print(i,end=" ")
    
