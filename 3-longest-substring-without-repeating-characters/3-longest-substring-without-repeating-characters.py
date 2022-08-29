class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s ==" " or len(s)==1:
            return 1
        
        i=0
        j=0
        store=""
        longest=""
        while i < len(s):
            if s[i] in store:
                if len(longest) < len(store):
                    longest = store 
                store=""    
                j+=1
                i=j
                
            else:    
                store=store+s[i]
                i += 1
                # print("i=",i)
                # if len(longest) < len(store):
                #     longest = store   
                #     print("longest=",longest,store)
                #     store=""
                    
                    # index=s.index(s[i])
                    # print("--",index)
                    # for j in range(index,i):
                    #     print("j-",j)
                    #     if s[j] not in store:
                    #         store=store+s[j]
                    #         print("store=",store)
        
        # print(store, len(longest))
        if len(longest) < len(store):
            longest = store   
            
        return len(longest)         