class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [x for x in s]
        t = [y for y in t]
        s.sort()
        t.sort()
        print(s, t)
        if s == t:
            return True
        else ：
        return False


a = Solution()
s = "anagram"
t = "nagaram"
a.isAnagram(s,t)
