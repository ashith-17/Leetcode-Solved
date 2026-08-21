class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        size = 1 << n

        # lcm[mask] = LCM of all coins represented by mask
        lcm = [1] * size

        for mask in range(1, size):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit

            lcm[mask] = lcm[prev] // gcd(lcm[prev], coins[i]) * coins[i]

        def count(x):
            total = 0

            for mask in range(1, size):

                amount = x // lcm[mask]

                if mask.bit_count() % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        low = 1
        high = min(coins) * k

        while low < high:

            mid = low + (high - low) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low