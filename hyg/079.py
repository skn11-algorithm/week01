n = int(input())
sum = 0

for i in range(1,1001):
    if n <= sum:
        print(i-1)
        break
    sum += i