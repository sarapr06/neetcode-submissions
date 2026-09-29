class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #can make a graph where directed b-> a
        #check to see if any cycles in the graph by dfs

        #1. build graph
        preMap={i:[] for i in range(numCourses)} #make a map with number of courses

        #2. use visiting set to track current dfs
        for course, prereq in prerequisites:
            preMap[course].append(prereq) #add prereq to the course graph

        #3. for each course, run dfs. if course already in visisting, return false. recursively dfs its prereqs
        visiting = set()
        def dfs(course):
            if course in visiting:
                #detect a cycle
                return False
            if preMap[course]==[]:
                return True #can finish
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False #if cycle in course
            #4. after processing a course, clear prereq list (mark as done)
            visiting.remove(course)
            preMap[course]=[] #passed
            return True
        #5. if all courses processed without cycles, return true
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True