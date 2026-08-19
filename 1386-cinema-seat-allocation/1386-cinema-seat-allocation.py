class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
       
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        ans = (n - len(rows)) * 2

        for row in rows:

            seats = rows[row]

            left = True
            middle = True
            right = True

            for seat in [2, 3, 4, 5]:
                if seat in seats:
                    left = False
                    break

            for seat in [4, 5, 6, 7]:
                if seat in seats:
                    middle = False
                    break

            for seat in [6, 7, 8, 9]:
                if seat in seats:
                    right = False
                    break

            if left and right:
                ans += 2

            elif left or middle or right:
                ans += 1

        return ans