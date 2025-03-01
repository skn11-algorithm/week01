h,w=map(int,input().split())
n=int(input())
arr=[[0]*(w) for _ in range(h)]

for _ in range(n):
    l,d,x,y=map(int,input().split()) #길이,방향(가로0,세로1),좌표 

    for _ in range(l):
        if d==0:
            arr[x-1][y-1]=1
            y+=1
        else:
            arr[x-1][y-1]=1
            x+=1

for i in range(h):
    print(*arr[i])