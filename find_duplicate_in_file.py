class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        

        contents = defaultdict(list)
        for p in paths:
            p = p.split()
            directory = p[0]

            for _file in p[1:]:
                _file = _file.split("(")
                content = _file[1]
                file_name = _file[0]
                contents[content].append(directory + "/" + file_name)
        res = []
        for content in contents:
            if len(contents[content]) > 1:
                res.append(contents[content])
        return res


