class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        indices_to_remove = set()
        stack = []
        for i, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack.append(i)
            elif not stack:
                indices_to_remove.add(i)
            else:
                stack.pop()
            
        # cast stack to set to make union operation work
        indices_to_remove = indices_to_remove.union(set(stack)) 

        string_builder = []
        for i, char in enumerate(s):
            if i not in indices_to_remove:
                string_builder.append(char)
        return "".join(string_builder)
    
    # Time: O(n), Space: O(n)