class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Store (value, original index)
        pairs = []

        for i in range(n):
            pairs.append((nums[i], i))

        # Sort by value
        pairs.sort()

        result = [0] * n

        i = 0

        while i < n:

            j = i

            # Find one connected group.
            # If consecutive values differ by <= limit,
            # they can be connected through swaps.
            while j + 1 < n and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1

            # Collect original indices of this group
            indices = []

            for k in range(i, j + 1):
                indices.append(pairs[k][1])

            # The values are already sorted because pairs is sorted.
            # Sort the original indices so the smallest values
            # go to the smallest positions.
            indices.sort()

            # Assign sorted values to sorted indices
            position = 0

            for k in range(i, j + 1):
                value = pairs[k][0]
                index = indices[position]

                result[index] = value

                position += 1

            # Move to the next group
            i = j + 1

        return result 