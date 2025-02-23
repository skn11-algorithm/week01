a = ['SUN','MON','TUE','WED','THU','FRI','SAT']
b = [31,28,31,30,31,30,31,31,30,31,30,31]

m,d = map(int,input().split())
days = d
for i in range(0,m-1):
    days += b[i]

result = days%7
print(a[result])