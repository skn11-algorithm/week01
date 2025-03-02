n=int(input())
hap=0
i=1
while True:
    hap+=i
    i+=1
    if hap>=n:
        break
print(hap)