class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        filtered_s = ""
        for i in s:
            if i in a_s:
                if i in a_s[26:52]:
                    filtered_s += i.lower()
                else:
                    filtered_s += i
        
        return filtered_s == filtered_s[::-1]
