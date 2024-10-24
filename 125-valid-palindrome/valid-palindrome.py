class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1
        
        while left < right:
            if s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1
            else:
                if (s[left].lower() != s[right].lower()):
                    return False
                
                left += 1
                right -= 1
        
        return True
         