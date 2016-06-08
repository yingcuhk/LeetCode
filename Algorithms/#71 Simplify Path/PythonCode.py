class Solution(object):
    """
    Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
    """
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        DirSeg = path.split('/')
        print DirSeg
        Candidate = []
        SimpliedPath = ""
        for seg in DirSeg:
            if seg == '.' or len(seg) == 0:
                continue
            if seg == '..':
                if len(Candidate) > 0:
                    Candidate = Candidate[:-1]
                #else:
                #    Candidate.append(seg)
            else:
                Candidate.append(seg)
        if len(Candidate) == 0:
            return "/"
        for seg in Candidate:
            SimpliedPath += "/"
            SimpliedPath += seg
        return SimpliedPath