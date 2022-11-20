#  252. Meeting Rooms


def meetRoom(intervals):
    intervals.sort(key=lambda i: i[0])
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start < prevEnd:
            return False
    return True


print(meetRoom([[0, 30], [5, 10], [15, 20]]))
print(meetRoom([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(meetRoom([[1, 7], [5, 8], [9, 7]]))
print(meetRoom([[1, 3], [3, 5], [5, 7], [8, 9]]))
