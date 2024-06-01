class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or any(len(item) == 0 for item in strs):
            return ""
        
        common = strs[0]
        for item in strs:
            while item.find(common) != 0:
                common = common[0:len(common)-1]
                if common == "":
                    return ""
        return common
        