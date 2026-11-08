class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) <=1 :
            return True

        cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", s.lower())


        y = len(cleaned_text) - 1

        for x in range (len(cleaned_text)) : 
            if cleaned_text[x] != cleaned_text[y] :
                return False
            if x == y :
                return True
            y = y -1             


        return True
