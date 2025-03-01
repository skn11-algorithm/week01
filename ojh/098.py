arr=[ list(map(int,input().split())) for _ in range(10)]

dx=[0,1]
dy=[1,0]
x,y=1,1
arr[x][y]=9

while True:
    moved=False #이동 여부

    for i in range(2):
        nx,ny=x+dx[i],y+dy[i]

        if arr[nx][ny]==2:
            arr[nx][ny]=9
            moved=True
            break
           
        if arr[nx][ny]==0:
            arr[nx][ny]=9
            x,y=nx,ny  
            moved=True     
            break # 오른쪽으로 갈 수 없을때만 밑으로 가야해서
    
    if not moved:  # 더 이상 이동할 곳이 없으면 종료
        break

for row in arr:
    print(*row)