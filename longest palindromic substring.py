class Solution:
    def longestPalindrome(self, s: str) -> str:# TC=O(n^2)
        size=len(s)
        ans=1
        f_l=0
        f_r=0
        for i in range(0,size):# for each character
            #expand outwards
            max_len_odd=1
            l_o=i-1
            r_o=i+1
            #covers odd length
            while l_o>=0 and r_o<size:
                if s[l_o]==s[r_o]:
                    max_len_odd=max_len_odd+2
                else:
                    break
                l_o=l_o-1
                r_o=r_o+1
            #covers even length
            max_len_even=0
            l_e=i-1
            r_e=i
            while l_e>=0 and r_e<size:
                if s[l_e]==s[r_e]:
                    max_len_even=max_len_even+2
                else:
                    break
                l_e=l_e-1
                r_e=r_e+1
            #compare between max_len_even, max_len_odd and ans and assign it to f_l(f_r)  to corresponding l_o or l_e(r_o or r_e)
            # print(i,ans,max_len_even,max_len_odd,f_l,f_r)
            if ans>=max_len_even and ans>=max_len_odd:
                continue
            elif max_len_even>max_len_odd:
                ans=max_len_even
                f_l=l_e+1
                f_r=r_e-1
            elif max_len_odd>max_len_even:
                ans=max_len_odd
                f_l=l_o+1
                f_r=r_o-1
        
        return s[f_l:f_r+1]
            
                
                
