class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic={}
        
        for i in range(len(words)):
            dic[words[i]] = dic.get(words[i],0)+1
        print(dic)
        
        arr=[]
        maxval=0
        
        for i in sorted(dic.items(),key=lambda v:(-v[1], v[0])):
            if k!=0:
                arr.append(i[0])
                k-=1
            print(arr)
        # print(sorted(arr))
        return arr
            
            