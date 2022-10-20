class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        
        if len(s) != len(t):
            return False
        elif sortedS == sortedT:
            return True
        