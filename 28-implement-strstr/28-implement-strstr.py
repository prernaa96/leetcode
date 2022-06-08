class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            ind = haystack.index(needle)
            print("ind-",ind)
            return ind
        else:
            return -1