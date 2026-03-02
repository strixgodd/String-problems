class Solution:
    # def frequencySort(self, s: str) -> str:
    #     freq={}
    #     for ch in s:
    #         if ch in freq:
    #             freq[ch]+=1
    #         else:
    #             freq[ch]=1
    #     freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))# sorted() returns a sorted list
    #     ans=""
    #     for key,value in freq.items():
    #         for i in range(0,value):
    #             ans=ans+key
    #     return ans
    
    def frequencySort(self, s: str) -> str:# optimized
        freq={}
        for ch in s: # SC=TC=O(n)
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        # key as frequency and list as velues corresponding to a particular key SC=TC=O(n)
        bucket={}
        for ch in freq:
            if freq[ch] in bucket:
                bucket[freq[ch]].append(ch)
            else:
                bucket[freq[ch]]=[ch]

        # create the ans from bucket dictionary TC=O(n)
        ans=""
        for i in range(len(s),0,-1):
            if i in bucket:
                for ch in bucket[i]:
                    ans=ans+ch*i # "a"*3="aaa"
        return ans



        
