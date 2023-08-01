import time
#how much is not taxed
def SellWithoutTax():
    f = open('new_register.txt','r')
    try:
        arrayline = f.readlines()
        sum = 0.0
        i = 0
        arr = arrayline[i].split(',', 2)
        while (time.time() - float(arr[1])) >= 31536000.0:
            sum += float(arr[0])
            i += 1
            arr = arrayline[i].split(',', 2)
        print("can sell without tax:", sum)
        return sum, i
    finally:
        f.close()

#benefit from not taxed
def Benefit(sum, firsttax,price):
    f = open('new_register.txt','r')
    try:
        totalprice = 0.0
        arrayline = f.readlines()
        for i in range(0, firsttax):
            arr = arrayline[i].split(',', 2)
            totalprice += float(arr[0]) * float(arr[2])
        print("had payed:", totalprice)
        print("will get:", sum * price)    
        print("benefit:", sum*price - totalprice)
        return (sum*price - totalprice)
    finally:
        f.close()

#add new line
def AddLine():
    text = []
    print("number of coins:")
    text.append(input())
    text.append(str(time.time()))
    print("price:")
    text.append(input())
    print(text)
    f = open('register_copi.txt','a')
    text = ", ".join(text)
    text += "\n"
    print(type(text))
    f.write(text)
    f.close()
    print("ok")