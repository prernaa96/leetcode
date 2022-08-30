class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        res = int("".join(map(str, digits))) + 1
        ans = [int(x) for x in str(res)]
        return ans 