class Solution:
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def add_words(i):
            line = []
            n_chars = 0
            
            while i < len(words) and n_chars + len(words[i]) <= maxWidth:
                line.append(words[i])
                n_chars += len(words[i]) + 1
                i += 1
            
            return line
        
        def create_line(line, i):
            unspaced_length = -1
            for word in line:
                unspaced_length += len(word) + 1
            
            spaces = maxWidth - unspaced_length
            
            if i == len(words) or len(line) == 1:
                return " ".join(line) + " " * spaces
                
            # distribute spaces between words
            gaps = len(line)-1
            min_spaces_per_gap = spaces // gaps
            remaining_spaces = spaces % gaps
            
            for j in range(gaps):
                line[j] += " " * min_spaces_per_gap
            
            for j in range(remaining_spaces):
                line[j] += " "
                
            return " ".join(line)
        
        output = []
        i = 0
        
        while i < len(words):
            curr = add_words(i)
            i += len(curr)
            output.append(create_line(curr, i))
            
        return output
            
            