class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        c=0
        maxval=0
        
        for i in sentences:
            c=i.count(" ")
            if c>maxval:
                maxval=c
        return maxval+1
            