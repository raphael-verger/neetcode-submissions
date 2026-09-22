# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while(True):
            if(not l1 and not l2 and carry ==0):
                break

            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry
            if (total<=9):
                carry = 0
                node = ListNode(total)
                tail.next = node
                tail = tail.next 
            else:
                carry = 1
                node = ListNode(total%10)
                tail.next = node
                tail = tail.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


        