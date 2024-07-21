class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping_st = {}
        mapping_ts = {}
        for letter_s, letter_t in zip(s, t):
            if letter_s not in mapping_st and letter_t not in mapping_ts:
                mapping_st[letter_s] = letter_t
                mapping_ts[letter_t] = letter_s
            elif mapping_st.get(letter_s) != letter_t or mapping_ts.get(letter_t) != letter_s:
                return False
            
        return True
    
    # Time: O(n), Space: O(1)
        