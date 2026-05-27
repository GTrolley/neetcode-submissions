class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp = ""

        for i in s:
            if i.isalnum():
                s_temp += i
        
        s_opp = s_temp[::-1].lower()

        if s_temp.lower() == s_opp:
            return True
        return False