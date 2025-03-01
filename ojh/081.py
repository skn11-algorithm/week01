n=int(input(),16) #입력을 16진수로 받고 10진수 변환
for i in range(1,16):
    print("%X*%X=%X"%(n,i,(n*i)))