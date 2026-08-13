class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        # Each node:
        # [left_char, right_char, prefix, suffix, best]
        tree = [[None, None, 0, 0, 0] for _ in range(4 * n)]

        def merge(node, left, right):
            mid = (left + right) // 2

            left_node = tree[node * 2]
            right_node = tree[node * 2 + 1]

            # Copy the boundary characters
            tree[node][0] = left_node[0]
            tree[node][1] = right_node[1]

            # Best answer completely inside either child
            best = max(left_node[4], right_node[4])

            prefix = left_node[2]
            suffix = right_node[3]

            # Can we connect the two children?
            if left_node[1] == right_node[0]:

                # A repeating run crosses the middle
                best = max(
                    best,
                    left_node[3] + right_node[2]
                )

                # Left child is completely one character
                left_length = mid - left + 1

                if left_node[2] == left_length:
                    prefix = left_length + right_node[2]

                # Right child is completely one character
                right_length = right - mid

                if right_node[3] == right_length:
                    suffix = right_length + left_node[3]

            tree[node][2] = prefix
            tree[node][3] = suffix
            tree[node][4] = best

        def build(node, left, right):

            if left == right:
                ch = s[left]

                tree[node][0] = ch
                tree[node][1] = ch
                tree[node][2] = 1
                tree[node][3] = 1
                tree[node][4] = 1
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            merge(node, left, right)

        def update(node, left, right, index, ch):

            if left == right:
                tree[node][0] = ch
                tree[node][1] = ch
                tree[node][2] = 1
                tree[node][3] = 1
                tree[node][4] = 1
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, ch)
            else:
                update(node * 2 + 1, mid + 1, right, index, ch)

            merge(node, left, right)

        # Build the initial segment tree
        build(1, 0, n - 1)

        answer = []

        for i in range(len(queryCharacters)):

            index = queryIndices[i]
            ch = queryCharacters[i]

            # Change one character
            update(1, 0, n - 1, index, ch)

            # Root contains the answer for the entire string
            answer.append(tree[1][4])

        return answer