class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs =defaultdict(list)
        doable = set()
        notDoable = set()
        for course ,pre in prerequisites:
            prereqs[course].append(pre)
            
        def canDo(course, doing) ->bool:
            if course in doable : return True
            if course in notDoable : return False
            for pre in prereqs[course]:
                if pre in doing:
                    notDoable.add(pre)
                    return False
                else:
                    doing.add(pre)
                    if not canDo(pre , doing):
                        notDoable.add(pre)
                        return False
                    doing.remove(pre)
            doable.add(course)
            return True

        for i in range(numCourses):
            if not canDo(i, set()): return False
        return True




                    



            

        

