class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""  # Contains only the alphanumeric values

        for c in s:
            if c.isalpha():
                newString += c.lower()
            if c.isnumeric():
                newString += c

        if (newString == newString[::-1]):
            return True
        else:
            return False
