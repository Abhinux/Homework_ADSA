array=[2,4,6,3,5,9,6,7,4,3]
n=len(array)
curr_sum=0
max_sum=0
x=0
y=0
k=int(input())
# for s in range(n-k+1):
#     for j in range(s,s+k):
#         curr_sum+=array[j]

#     if curr_sum>max_sum:
#         max_sum=curr_sum
#         x=s
#         y=s+k-1
#     curr_sum=0
# print(max_sum)
# print(x)
# print(y)
    
l=0
r=k
for i in range(l,r-1):
    curr_sum+=array[i]
while(r<n):
    curr_sum+=array[r-1]
    if curr_sum>max_sum:
        max_sum=curr_sum
        x=l
        y=r-1
    curr_sum-=array[l]
    l+=1
    r+=1

print(max_sum)
print("starting index:",x)
print("Ending index:",y)


