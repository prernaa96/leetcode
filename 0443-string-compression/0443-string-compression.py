class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        i=0
        count=1
        for j in range(1,n+1):
            if j<n and chars[j]==chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i+=1
                if count>1:
                    for k in str(count):
                        chars[i] = k
                        i+=1
                count = 1
        chars = chars[:i]
        return i
        
        
        
#         if len(chars)==1:
#             return 1
        
#         i=0
#         j=1
#         while(i<j):
#             print(chars[i], chars[j], i,j)
            
#             if chars[i] == chars[j]:
#                 print(i,j)
#                 j+=1
#                 print("first if",j)
            
#             if j==len(chars):
#                 length=j-i-1
                
#                 for k in range(length):
#                     print("l==>>--",length)
#                     del chars[i+1]
#                     print("in--",chars)
#                 # print("l==>>",length)
#                 if length>1:
#                     if length>10:
#                         for x in str(length):
#                             chars.insert(i+1, str(x))
#                     else:
#                         chars.insert(i+1, str(length))
#                 print("--//>",chars)
            
#                 return len(chars)
            
#             if chars[i] != chars[j]:
#                 length=j-i
#                 # print(length,j,i)
#                 for k in range(length-1):
#                     del chars[i+1]
#                     print(chars)
                
#                 print("l==",length)
                
#                 if length>1:
#                     if length>10:
#                         for x in str(length):
#                             chars.insert(i+1, str(x))
#                     else:
#                         chars.insert(i+1, str(length))
#                 print("-->",chars)
                
#                 if length!=1:
#                     i+=2
#                 else:
#                     i+=1
#                 j=i+1
#                 print("len==",length)
                
#                 length=0
                
                
            
            
            
                
            
                
        
        
            
        