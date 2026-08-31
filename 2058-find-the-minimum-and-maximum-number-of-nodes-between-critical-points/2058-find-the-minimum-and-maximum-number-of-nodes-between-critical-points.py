# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        position = 1

        prev = head
        curr = head.next

        first_critical = -1
        previous_critical = -1

        min_distance = float('inf')
        max_distance = -1

        while curr.next is not None:

            next_node = curr.next

            # Check whether curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                # This is the first critical point
                if first_critical == -1:
                    first_critical = position

                else:
                    # Distance from previous critical point
                    distance = position - previous_critical

                    if distance < min_distance:
                        min_distance = distance

                # Update previous critical point
                previous_critical = position

                # Distance from first to current
                max_distance = position - first_critical

            prev = curr
            curr = next_node
            position += 1

        # Fewer than two critical points
        if first_critical == -1 or first_critical == previous_critical:
            return [-1, -1]

        return [min_distance, max_distance]