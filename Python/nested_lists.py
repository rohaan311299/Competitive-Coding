import numpy as np

N=int(input())
marksheets=[]
names=[]
for i in range(0,N):
    # name=input()
    marks=float(input())
    marksheets.append(marks)
# print(marksheets)
marksheets_array=np.array(marksheets)
# print(np.unique(marksheets_array))
sorted_array=np.sort(marksheets_array)
print(sorted_array[1])

'''
n = int(input())
marksheet = []
for _ in range(0,n):
    marksheet.append([input(),float(input())])

sechigh=sorted(list(set(marks for name, marks in marksheet)))[1]

print("\n".join([a for a,b in sorted(marksheet) if b == sechigh]))

'''