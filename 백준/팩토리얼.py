num=int(input(""))
factorial = 0
for a in range(0,num+1):
    if num==0:
        factorial=1
        break
    elif a==1:
        factorial+=1
    else:
        factorial*=a
print(factorial)