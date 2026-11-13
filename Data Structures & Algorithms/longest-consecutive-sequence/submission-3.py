class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)

        lon = 0

        for n in numsset:
            if (n-1) not in numsset:
                lenght = 1

                while (n+lenght) in numsset:
                    lenght += 1
                
                lon = max(lenght, lon)
        
        return lon