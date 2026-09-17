class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        i, j = 0, len(cleaned)

        while(i<j):
            if cleaned[i]!= cleaned[j-1]:
                return False
            i=i+1
            j=j-1
        return True