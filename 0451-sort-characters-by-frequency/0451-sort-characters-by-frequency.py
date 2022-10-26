class Solution:
    def frequencySort(self, s: str) -> str:
        
        # 1. create dict
        # 2. loop dict in desc order of values
        # 3. add chars to a string => char*count
        
        dic=Counter(s)
        string=""
        for key in sorted(dic, key=dic.get, reverse=True):
            string+= key*dic[key]
        
        return string