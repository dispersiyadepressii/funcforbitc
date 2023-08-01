import time
SEC_IN_YEAR = 31536000.0

#function returns data fron text in list(array)
def readStateFile(nameoffile):
    with open(nameoffile,'r') as f:
        arrdata = f.readlines()
        if arrdata != None:
            return arrdata
        else:
            print("Error, empty file, try another one")
            return 0
        
#check the order by date        
def checkOrderByDate(arrdata):
    previousdate = 0.0
    for i in range(0, len(arrdata)):
        arrline  = arrdata[i].split(',', 2)
        if float(arrline[1]) < previousdate:
            print("array doesnt ordered by date")
            print("previousdate:", previousdate, "date:", arrline[1]) 
            return 1
        previousdate = float(arrline[1])
    return 0

# sorting by time btw
def SortByDate(strings):
    sorted_strings = sorted(strings, key=lambda line: float(line.split(",")[1]))
    return sorted_strings

#how much is not taxed
def SellWithoutTax(arrdata):
    sum = 0.0
    for i in range(0, len(arrdata)):
        arrline  = arrdata[i].split(',', 2)
        if (time.time() - float(arrline[1])) >= SEC_IN_YEAR:
            sum += float(arrline[0])
    print("can sell without tax:", sum)
    return sum

#counting benefit 
def Benefit(sum, price, arrdata):
    hadpaid = 0.0
    taxable = 0.0
    for i in range(0, len(arrdata)):
        if int(sum) == 0:
            break
        else:
            arrline = arrdata[i].split(',', 2)
            if float(arrline[0]) >= sum:
                hadpaid += sum*float(arrline[2])
                if (time.time() - float(arrline[1])) <= SEC_IN_YEAR:
                    taxable += sum*float(arrline[2])
                sum = 0.0
            else:
                hadpaid += float(arrline[0]) * float(arrline[2])
                if (time.time() - float(arrline[1])) <= SEC_IN_YEAR:
                    taxable += float(arrline[0]) * float(arrline[2])
                sum -= float(arrline(0))
    if sum != 0.0:
        print("insufficient funds, missing", sum, "BTC")
        return 0
    else:
        print("had payed:", hadpaid)
        print("will get:", sum * price)    
        print("benefit:", sum*price - hadpaid)
        return (sum*price - hadpaid)

#def Benefit(sum, firsttax, price):
 #   arrayline = ReadLines('new_register.txt')
#  totalprice = 0.0
 #   for i in range(0, firsttax):
  #      arr = arrayline[i].split(',', 2)
   #     totalprice += float(arr[0]) * float(arr[2])
    #print("had payed:", totalprice)
    #print("will get:", sum * price)    
    #print("benefit:", sum*price - totalprice)
    #return (sum*price - totalprice)


#add new line
def AddLine():
    text = []
    print("number of coins:")
    text.append(input())
    text.append(str(time.time()))
    print("price:")
    text.append(input())
    print(text)
    with open('register_copi.txt','a') as f:
        text = ", ".join(text)
        text += "\n"
        print(type(text))
        f.write(text)
        f.close()
    print("ok")