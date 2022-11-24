class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # 1. If trans is more than>1000: add i to ans
        # 2. dict=> name:{time,city}
        # 3. (1)
        # 4. if time diff<60: , city diff and name same - both invalid. Add to ans
            
        
        out = [] #list of all the invalid transactions to return 
        names = defaultdict(lambda: defaultdict(set)) #{name: {time: city}}


        for t in transactions:
            name,time,amount,city = t.split(",")
            names[name][time].add(city)

        #-if a certain person is at more than one city at a time then we know it's an invalid transaction
        #-if the city we're at is not in the set it means the transaction has been made at two places within the 60 min limit

        for t in transactions:
            name, time, amount, city = t.split(",")
            if int(amount) > 1000:
                out.append(t)            
            else:
                for num in names[name].keys():
                    if -60 <= int(time) - int(num) <= 60 and (len(names[name][num]) > 1 or city not in names[name][num]):
                        out.append(t)
                        break

        return out
            
            
            
            
            
            