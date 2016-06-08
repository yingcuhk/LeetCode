class Solution(object):
    
    """
    There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        Visited = list([0]*numCourses)
        edges = list(prerequisites)
        for curnode in xrange(numCourses):
            if Visited[curnode]:
                continue
            Marked = list([0]*numCourses)
            Loop, Visited, Marked = self.DFS(edges,Visited,Marked,curnode)
            if Loop == False:
                return False
            remainEdges = edges
            for edge in edges:
                if Visited[edge[0]] or Visited[edge[1]]:
                    remainEdges.remove(edge)
            edges = remainEdges
        return True
    def DFS(self,edgeSet,Visited,Marked,curnode):
        
        Visited[curnode] = 1
        Marked[curnode] = 1
        for edge in edgeSet:
            if edge[0] == curnode:
                nextNode = edge[1]
                if Marked[nextNode]:
                    return False, Visited, Marked
                else:
                    temploop, Visited, Marked = self.DFS(edgeSet, Visited, Marked, nextNode)
                if temploop == False:
                    return False, Visited, Marked
                else:
                    Marked[nextNode] = 0
        
        return True, Visited, Marked
        
