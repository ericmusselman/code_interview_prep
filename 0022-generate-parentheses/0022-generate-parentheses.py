class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(current_string, left_count, right_count):
            if len(current_string) == 2*n:
                answer.append("".join(current_string))
                return
            if left_count < n:
                current_string.append("(")
                backtracking(current_string, left_count + 1, right_count)
                current_string.pop()
            if right_count < left_count:
                current_string.append(")")
                backtracking(current_string, left_count, right_count + 1)
                current_string.pop()
                
        backtracking([], 0, 0)
        return answer
    
    # Space: O(n), Time: ...