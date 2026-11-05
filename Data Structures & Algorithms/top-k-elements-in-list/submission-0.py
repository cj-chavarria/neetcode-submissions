class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)

        for n in nums:
            hash[n] += 1
        
        sort = sorted(hash.items(), key=lambda x: x[1], reverse=True)[:k]

        return [x[0] for x in sort]