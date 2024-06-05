class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return []
        
        number_letter_key = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        combos = []
        
        def backtrack(i, wip):
            """
            i: index of letter we are on: int
            wip:string of letters being built, not complete (wip) : str
            """
            if len(wip) == len(digits): # complete
                combos.append("".join(wip)) # append
                return
        
            next_letters = number_letter_key[digits[i]] # next letter options
            for letter in next_letters: # loop the next letter options
                wip.append(letter) # append letter
                backtrack(i+1, wip) # move to the next one
                wip.pop() # remove letter at current step to consider next letter in this loop
        
        backtrack(i=0,wip=[]) # start at first index, pass empty list of letters to build from
        return combos
    