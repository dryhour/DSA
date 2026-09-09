# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        number1 = 0
        count = 0
        while l1:
            number1 += (l1.val * (10 ** count))
            count += 1
            l1 = l1.next

        number2 = 0
        count = 0
        while l2:
            number2 += (l2.val * (10 ** count))
            count += 1
            l2 = l2.next
        # number1 = l1.val + l1.next.val*10 + l1.next.next.val*100
        # number2 = l2.val + l2.next.val*10 + l2.next.next.val*100

        result = str(number1 + number2)
        newNode = ListNode(int(result[-1]))
        finalNode = newNode

        for i in range(1, len(result)):
            newNode.next = ListNode(int(result[-(i+1)]))
            newNode = newNode.next
        return finalNode
        