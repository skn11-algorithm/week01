n = int(input())
a = list(map(int, input().split()))
idx=n-1

while True:
  if idx==-1:
    break
  print(a[idx], end=' ')
  idx -= 1
