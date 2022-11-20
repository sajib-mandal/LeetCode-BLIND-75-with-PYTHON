#  253. Meeting Rooms II 

import heapq
def meetRoomII(intervals):
    intervals.sort(key=lambda i: i[0])
    count = 1
    heap = [intervals[0][1]]
    for start, end in intervals[1:]:
        if heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        count = max(count, len(heap))
    return count


print(meetRoomII([[0, 30], [5, 10], [15, 20]]))
print(meetRoomII([[7, 10], [2, 4]]))
