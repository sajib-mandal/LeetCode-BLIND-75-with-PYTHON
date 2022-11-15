#  207. Course Schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # *
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        
        noPreCourses = [n for n in range(numCourses) if not courses[n]]
        count = 0
        while noPreCourses:
            noPre = noPreCourses.pop()
            count += 1
            for course in pres[noPre]:
                courses[course].remove(noPre)
                if not courses[course]:
                    noPreCourses.append(course)
        return count == numCourses
        
        
        
        
        
        
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
