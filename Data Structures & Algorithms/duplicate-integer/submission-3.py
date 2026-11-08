class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = defaultdict(int)

        for n in nums:
            res[n] += 1
            
            if res[n] > 1:
                return True

        return False        