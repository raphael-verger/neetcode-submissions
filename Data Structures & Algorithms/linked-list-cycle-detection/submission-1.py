class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Pointers meet at the exact same node in memory
                return True

        return False
