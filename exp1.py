#example python program to recieve multiple inputs simultaneously
#no .of test cases
t=int(input())
for i in range(0,t):
  #using map function we enter multiple inputs
  x,y=map(int,input().split())
  print("sum =",x+y)
  print("power =",x**y)
  
  
