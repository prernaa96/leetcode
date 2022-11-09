class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        print(moves.count("U"))
        print(moves.count("D"))
        print(moves.count("R"))
        print(moves.count("L"))
        
        # if moves.count("U") == moves.count("D") or moves.count("R")== moves.count("L"):
        #     print("1--")
        #     return True
        if moves.count("U") == moves.count("D") and moves.count("R")== moves.count("L"):
            print("2--")
            return True
     
        return False
        