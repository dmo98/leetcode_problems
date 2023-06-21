class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Use a HashSet
        jewels = set(jewels)
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        return total