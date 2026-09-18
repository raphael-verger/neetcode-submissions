class Solution:

    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 1. Advance right pointer so gap between left and right is n
        for _ in range(n):
            right = right.next

        # 2. Move both until right falls off the end
        while right:
            left = left.next
            right = right.next

        # 3. Skip the target node
        left.next = left.next.next

        return dummy.next
