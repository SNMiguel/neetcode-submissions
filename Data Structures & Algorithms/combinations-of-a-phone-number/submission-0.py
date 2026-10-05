class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wyxz"
        }

        if not digits:
            return []
        
        res = []

        def backtracking(cur_char, index):
            if len(cur_char) == len(digits):
                res.append(cur_char)
                return
            
            for letter in letters[digits[index]]:
                backtracking(cur_char + letter, index + 1 )

        backtracking("", 0)
        return res