n=int(input())
check=[0]*(24)
for num in map(int,input().split()):
    check[num]+=1
print(*check[1:24])
