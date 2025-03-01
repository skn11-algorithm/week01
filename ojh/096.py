baduk=[]
for _ in range(19):
    arr=list(map(int,input().split()))
    baduk.append(arr)

n=int(input())
for i in range(n):
    x,y=map(int,input().split())
  
    for j in range(19):
        # if baduk[x-1][j]==1:
        #     baduk[x-1][j]=0
        # else:
        #     baduk[x-1][j]=1
        # if baduk[j][y-1]==1:
        #     baduk[j][y-1]=0
        # else:
        #     baduk[j][y-1]=1
        
        # 1이면 1-1=0, 0이면 1-0=1. 값 반전
        baduk[x-1][j]=1-baduk[x-1][j]
        baduk[j][y-1]=1-baduk[j][y-1]

for i in range(19):
    print(*baduk[i])
