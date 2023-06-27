class Solution:
    def simplifyPath(self, path: str) -> str:
        # split the path, using '/' as the delimiter, if segment is '.' ignore, if it's '..' then pop, else keep segment in final simplified path
        stack = []
        path_segments = path.split('/')
        print(path_segments)
        for segment in path_segments:
            if segment == '.' or segment == '':
                continue
            elif segment == '..':
                if stack != []:
                    stack.pop()
            else:
                stack.append(segment)
        return "/" + "/".join(stack)