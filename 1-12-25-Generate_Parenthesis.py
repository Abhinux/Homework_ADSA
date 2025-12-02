class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(p, left, right, parens=[]):
            if left:         
                gen(p+'(',left-1,right)
            if right > left: 
                gen(p+')',left,right-1)
            if not right:    
                parens+=p
            return parens
        return gen('',n,n)