class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic={}
        
        for i in strs:
            word = ''.join(sorted(i))
            
            if word in dic:
                dic[word] = dic[word]+[i]
            else:
                dic[word] = [i]
        
        return dic.values()
       