class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adjList[course].append(pre)
            
    
        seen = set()
        
        def dfs(course):
            if course in seen: # we have visted a course twice, cycle detected
                return False
            if adjList[course] == []: # if no prereqs, it can be done
                return True
            
            seen.add(course)
            
            # loop through prereqs for this course
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
                
            seen.remove(course)
            adjList[course] = [] # set this to empty list so it'll return True right away instead of repeating for loop
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            

       
                
        