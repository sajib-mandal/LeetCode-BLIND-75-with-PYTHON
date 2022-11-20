#   435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        count = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)
        return count
