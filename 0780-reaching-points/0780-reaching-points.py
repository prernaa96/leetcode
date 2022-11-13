class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        #Mod of tx = tx%ty and ty=ty%tx
        
        if sx==sy==tx==ty: return True
        
        while sx<tx and sy<ty:
            tx,ty=tx%ty,ty%tx

        #Main = (ty-sy)%sx ==0 and (tx-sx)%sy==0
        #Rest - edge cases
        
        if tx!=0 and ty!=0 :
            if sx==tx and sy<=ty and (ty-sy)%sx ==0 or sy==ty and sx<=tx and (tx-sx)%sy==0:
                return True
        
        return False