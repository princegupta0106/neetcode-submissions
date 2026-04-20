class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs =defaultdict(list)
        preCount = [0]*(numCourses)
        courseDone = 0
        for course ,pre in prerequisites:
            prereqs[pre].append(course)
            preCount[course] += 1
        q = deque()
        for i,x in enumerate(preCount):
            if not x :
                q.append(i)
        while q:
            course = q.popleft()
            courseDone += 1 
            for nei in prereqs[course]:
                preCount[nei] -=1
                if not preCount[nei]:
                    q.append(nei)
        return courseDone == numCourses
            


        


                    



            

        

