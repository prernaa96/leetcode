class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        kbc=0
        window = str(num)
        # window=window[:k+1]
        for i in range(len(window)-k+1):
            window2 = int(window[i:i+k])
            if (window2!=0 and num % window2==0):
                kbc+=1
        return kbc

            