a,b,c=map(int,input().split())
d=a
while True:
     if d%a==0 and d%b==0 and d%c==0:
         break
     d+=1
print(d)

# import math
# a,b,c=map(int,input().split())
# print(math.lcm(a,b,c))
