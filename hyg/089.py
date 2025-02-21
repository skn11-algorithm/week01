a,r,n = map(int, input().split())
result = a

for i in range(0,n-1):
    result *= r
print(result)