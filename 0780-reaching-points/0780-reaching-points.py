class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        if sx==sy==tx==ty: return True
        
        while sx<tx and sy<ty:
            tx,ty=tx%ty,ty%tx
            print(tx,ty)

        if tx!=0 and ty!=0 :
            if sx==tx and sy<=ty and (ty-sy)%sx ==0 or sy==ty and sx<=tx and (tx-sx)%sy==0:
                return True
        
        return False