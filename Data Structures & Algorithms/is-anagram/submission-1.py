class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqS, freqT = {}, {}

        for letter in s:
            freqS[letter] = freqS.get(letter, 0) + 1

        for letter in t:
            freqT[letter] = freqT.get(letter, 0) + 1

        return freqS == freqT
