# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        visited=set()
        
        while curr!=None:
            # print(visited,"\n")
            
            visited.add(curr)
            curr=curr.next
            if curr in visited:
                return True
                
        return False        