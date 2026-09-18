# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        sortedSet = set()
        
        topList = head
        while topList:
            sortedSet.add(topList.val)

            topList = topList.next

        sortedSet = sorted(list(sortedSet))

        if len(sortedSet) == 0:
            return None

        newNode = ListNode(sortedSet[0])
        current = newNode

        for i in range(1, len(sortedSet)):
            current.next = ListNode(sortedSet[i])
            current = current.next

        return newNode
