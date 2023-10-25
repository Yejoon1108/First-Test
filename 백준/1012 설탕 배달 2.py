num = int(input(""))
count = 0
while True:
    if num%5==0:
        count += num//5
        print(count)
        break
    num -= 3
    count += 1
    if num < 0 :
        print("?")
        break