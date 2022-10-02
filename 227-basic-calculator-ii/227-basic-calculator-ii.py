class Solution:
    def calculate(self, s: str) -> int:
        
        s=s.replace(" ","")
        s += '+'
        num=0
        op='+'
        arr=[]
        
        for i in s:
            if i.isdigit():
                num = (num*10) + int(i)
                # print("=====if")
            else:
                num=int(num)
                if op == "+":
                    arr.append(num)
                elif op == "-":
                    arr.append(-num)
                elif op == "*":
                    arr.append(arr.pop()*num)
                elif op=="/":
                     arr.append(int(arr.pop()/num))
                num=0
                op=i
                # print("op--",op, arr)
        # print(arr)
        return sum(arr)