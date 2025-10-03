class Solution:
	def prevSmaller(self, arr):
		# code here
		l=len(arr)	
		res=[-1]*l
		stck=[]
		for i in range(l):
		    while(stck!=[] and arr[i]<=stck[-1]):
		        stck.pop()
		    if stck!=[]:
		        res[i]=stck[-1]
		    stck.append(arr[i])
		
		return res