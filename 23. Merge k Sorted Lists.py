# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not len(lists)):
            return None
        
        sol = lists[0]
        for i in range(1, len(lists)):
            slist = lists[i]
            curNode = None
            rootNode = None
            tail = None
            while slist or sol:
                if(not sol or (slist and sol.val > slist.val)):
                    curNode = slist
                    slist = slist.next
                elif not slist or (sol and slist.val >= sol.val):
                    curNode = sol
                    sol = sol.next

                if(not rootNode):
                    rootNode = curNode
                if(not tail):
                    tail = curNode
                else:
                    tail.next = curNode
                    tail = tail.next
            
            sol = rootNode

        return sol