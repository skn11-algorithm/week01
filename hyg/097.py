h,w = map(int, input().split())
n = int(input())

m=[]
for i in range(h+1):
    m.append([])
    for j in range(w+1):
        m[i].append(0)

for i in range(n):
    l,d,x,y = map(int, input().split()) # 길이, 방향, 좌표
    for j in range(0,l):
        if d==0: #가로
            m[x][y+j] = 1
        else:
            m[x+j][y] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(m[i][j], end=' ')
    print()
