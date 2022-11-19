#   347. Top K Frequent Elements


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for key, val in freq.items():
            if len(res) < k:
                heapq.heappush(res, (val, key))
            else:
                heapq.heappushpop(res, (val, key))
        return [key for val, key in res]
        
        
        
        
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            res=[]
            dict = collections.Counter(nums)
            for val, count in dict.items():
                if len(res)<k:
                    heapq.heappush(res,(count,val))
                else:
                    heapq.heappush(res,(count,val))
                    heapq.heappop(res)
            return [val for count, val in res]
        
        
        
        
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res
