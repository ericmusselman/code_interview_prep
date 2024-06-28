class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s) == 0:
            return False
        
        words = s.split(" ")
        map_char = {}
        map_word = {}
        
        if len(words) != len(pattern):
            return False
        
        for el, word in zip(pattern, words):
            if el not in map_char:
                if word in map_word:
                    return False
                else:
                    map_char[el] = word
                    map_word[word] = el
            else:
                if map_char[el] != word:
                    return False
        return True
            
    # Time: O(n), Space: O(n)