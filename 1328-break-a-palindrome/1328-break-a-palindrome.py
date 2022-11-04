class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        
        # 1. If start letter is > a then a= start letter
        # 2. If start letter is smaller than next, change next letter to a
        # 3. If all letters same, change one letter with smallest letter possible
        
        if len(palindrome) ==1:
            return ""
        for i in palindrome:
            
            if len(set(palindrome)) ==1:
                ord_val = ord(palindrome[0])
                if ord_val > 97:
                    palindrome=palindrome.replace(palindrome[0], 'a', 1)
                    print(palindrome)
                    break
                else:
                    palindrome = palindrome[:-1]
                    palindrome+='b'
                    break
            elif ord(i)>97:
                palindrome=palindrome.replace(i,'a',1)
                break
            elif ord(i)==97:
                #aba, abcca
                old=palindrome
                index=palindrome.index(i)
                for j in palindrome[index+1:]:
                    if ord(j) >97:
                        palindrome=palindrome.replace(j,'a',1)
                        if palindrome==palindrome[::-1]:
                            palindrome=old[:-1]
                            palindrome+='b'
                        break
                break
        
        return palindrome