class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs =defaultdict(list)
        preCount = [0]*(numCourses)
        courseDone = 0
        for course ,pre in prerequisites:
            prereqs[pre].append(course)
            preCount[course] += 1
        q = deque()
        order = []
        for i,x in enumerate(preCount):
            if not x :
                q.append(i)
                order.append(i)

        while q:
            course = q.popleft()
            courseDone += 1 
            for nei in prereqs[course]:
                preCount[nei] -=1
                if not preCount[nei]:
                    q.append(nei)
                    order.append(nei)
        if courseDone == numCourses:
            return order
        return []
        