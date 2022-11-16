#   128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStack = 0
        for n in numSet:
            if (n - 1) not in numSet:
                currentNum = n
                currentStack = 1
                while (currentNum + 1) in numSet:
                    currentNum += 1
                    currentStack += 1
                longestStack = max(currentStack, longestStack)
        return longestStack
        
        
        
        
        
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
