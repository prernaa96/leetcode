class Solution:
    def reverse(self, x: int) -> int:
        
        
        strx = str(x)
        strx_rev = strx[::-1]
        if x < 0:
            strx_rev = strx_rev[:len(strx_rev)-1]
            strx_rev = '-' + strx_rev
        # print((int(strx_rev)))
        
        if x <= (-2 ** 31) or x >= ((2 ** 31)-1) or int(strx_rev) <= (-2 ** 31) or int(strx_rev) >= ((2 ** 31)-1):
            return 0
        return int(strx_rev)