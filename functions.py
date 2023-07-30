import time

def ReadLines(nameoffile):
    with open(nameoffile,'r') as f:
        arrayline = f.readlines()
        return arrayline

#how much is not taxed
def SellWithoutTax():
    arrayline = ReadLines('new_register.txt')
    sum = 0.0
    i = 0
    arr = arrayline[i].split(',', 2)
    while (time.time() - float(arr[1])) >= 31536000.0:
        sum += float(arr[0])
        i += 1
        arr = arrayline[i].split(',', 2)
    print("can sell without tax:", sum)
    return sum, i

#benefit from not taxed
def Benefit(sum, firsttax,price):
    arrayline = ReadLines('new_register.txt')
    totalprice = 0.0
    for i in range(0, firsttax):
        arr = arrayline[i].split(',', 2)
        totalprice += float(arr[0]) * float(arr[2])
    print("had payed:", totalprice)
    print("will get:", sum * price)    
    print("benefit:", sum*price - totalprice)
    return (sum*price - totalprice)


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