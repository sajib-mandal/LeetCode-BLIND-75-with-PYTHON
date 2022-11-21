#   242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(s + t), Space: O(s + t)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
    
        
        if len(s) != len(t):
            return False
        sMap = {}
        for letter in s:
            if letter in sMap:
                sMap[letter] += 1
            else:
                sMap[letter] = 1

        tMap = {}
        for letter in t:
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1

        for key in sMap:
            if key not in tMap:
                return False
            if not sMap[key] == tMap[key]:
                return False
        return True
