w,h,b = map(int, input().split())
mb = (w*h*b)/(1024*1024*8)
print(format(mb,'.2f'),'MB')