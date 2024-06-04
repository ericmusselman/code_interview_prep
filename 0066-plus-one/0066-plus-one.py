class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        reverse_digits = digits[::-1]
        for i in range(len(reverse_digits)):
            if reverse_digits[i] == 9:
                reverse_digits[i] = 0
                carry = 1
            else:
                reverse_digits[i] += 1
                return reverse_digits[::-1]
        
        if carry == 1:
            reverse_digits.append(1)
        return reverse_digits[::-1]