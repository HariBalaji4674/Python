#Pattern problems
#1  Square Pattern
# Outer Loop Represents the rows || no of lines == no of rows
# Inner Loop Represents the Columns

# Improve Thought process


for i in range(4):
  for j in range(4):
    print(i,end=" ")
  print()

#2
'''
* * * * *
* * * *
* * *
* *
*
'''

n =5
for i in range(n):
  for j in range(i+1):
    print(i,end=" ")
  print()

'''
* * * * *
* * * *
* * *
* *
*
'''

print("This is reverse array")

n = 5
for i in range(n,0,-1):
  for j in range(i):
    print(i,end=" ")
  print()

#1 Increasing Traingle
#2 Decreasing Traingle
#3 Right Sided Traingle

for i in range(n):
  for j in range(i):
    print('*',end=" ")
  print()

for i in range(n):
  for j in range(i,n):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  print()

# Increasing means = i+1
# Decreasing Means = i,n

for i in range(n-1):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i):
    print("*",end=" ")
  print()
for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i,n-1):
    print("*",end=" ")
  print()

k=0
for i in range(n):
  for j in range(i+1):
    print(k,end=" ")
    k+=1
  print()
for i in range(n):
  for j in range(i,n-1):
    print(k,end=" ")
  print()

for i in range(n):
  if i%2 == 0:
    start = 1
  else:
    start = 0
  for j in range(i+1):
    print(start,end=" ")
    start = 1-start
  print()