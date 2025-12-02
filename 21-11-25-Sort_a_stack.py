class Solution:
    def sortStack(self, st):
        # code here 
        if st!=[]:
            n=st.pop()
            self.sortStack(st)
            temp=[]
            while(st!=[] and st[-1]>n):
                temp.append(st.pop())
            st.append(n)
            while(temp!=[]):
                st.append(temp.pop())
