r,g,b=map(int,input().split())
stg=round(r*g*b/8/1024/1024,2)
print("%.2f MB"%stg)