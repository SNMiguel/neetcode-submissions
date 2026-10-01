class Solution:
    def isValid(self, s: str) -> bool:
        record = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        pile = []
        for i in s:
            if i not in record:
                pile.append(i)
            else:
                if pile:
                    if record[i] == pile[-1]:
                        pile.pop()
                    else:
                        return False
                        break
                else:
                    return False
                    break

        return not pile
