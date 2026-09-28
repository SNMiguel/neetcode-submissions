class Solution:

    def encode(self, strs: List[str]) -> str:
        rec = ""
        for s in strs:
            rec += f'{len(s)}#{s}'
        return rec

    def decode(self, s: str) -> List[str]:
        rec = []
        i = 0
        j = 0

        while i < len(s):
            if s[j] == "#":
                l = int(s[i:j])
                rec.append(s[j+1 : j+l+1])
                j += l+1
                i = j
            else:
                j += 1
        
        return rec