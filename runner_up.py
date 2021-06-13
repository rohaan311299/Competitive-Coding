'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
'''
n=int(input())
a=list(map(int,input().split()))

new_a=list(set(a))
new_a.sort()
print(new_a[-2])
