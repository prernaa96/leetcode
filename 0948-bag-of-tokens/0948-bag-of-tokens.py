class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
#         0. sort
        # 1. token[0]
        # 2. if power>=token[0] => power-token[0]  //power=100
        # 3. score+=1
        # 4. if score>=1
        # 5. token[len(token)-1] => power=power+token[len(token)-1] //500
        # 6. score-=1 
        
        tokens.sort()
        j=len(tokens)-1
        print("j=",j)
        i=0
        score=0
        maxscore=0
        
        if i==j and power<tokens[i]:
            return 0
        if len(tokens)==0:
            return 0
        
        while i<=(len(tokens)-1) and i<=j:
            print(tokens[i])
            if power>=tokens[i]:
                power=power-tokens[i]
                score+=1
                maxscore=max(score,maxscore)
                i+=1
                print("coming in--",score,power)
            else:
                print("in else")
                if score==0:
                    return 0
                if score>=1 and j>=0:
                    power=power+tokens[j]
                    score-=1
                    j-=1
                
            print("---->",power,score)
            print("i,j---->",i,j)
        
        return maxscore