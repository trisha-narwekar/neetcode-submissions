class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        
        result = sorted(lookup.items(), key=lambda x: x[1], reverse=True)
        top_n = [item[0] for item in result[:k]]
        return top_n