class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        sentence=set(sentence)
        if len(sentence)==26:
            return True
        return False
        
        # for i in sentence:
        #     print(ord(i))