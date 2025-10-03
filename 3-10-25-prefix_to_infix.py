class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        l=len(pre_exp)
        L=[]
        for i in range(l-1,-1,-1):
            match pre_exp[i]:
                case "*"|"/"|"+"|"-"|"^"|"%":
                    a=L.pop()
                    b=L.pop()
                    L.append("("+a+pre_exp[i]+b+")")
                case _:
                    L.append(pre_exp[i])
        return L[0]