class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        tot = 0
        
        for i in columnTitle:
            tot = tot*26 + ord(i)-64
        
        return tot
        
        