from math import factorial
class Solution:
    def countAnagrams(self, s: str) -> int:
        words=[]
        word=[]
        res=1
        for i in s:
            if i==" ":
                words.append(word)
                word=[]
            else:
                word.append(i)
        words.append(word)

        for i in words:
            n1=factorial(len(i))
            for j in Counter(i).values():
                n1//=factorial(j)
            res*=n1
            
        
        return res %(10**9+7)