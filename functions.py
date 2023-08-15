import time
SEC_IN_YEAR = 31536000.0

class Record(object):
    def __init__(self, quantity=0, data=0, price=0):
        self.quantity = quantity
        self.data = data
        self.price = price

    def purchase_amount(self):
        return float(self.quantity) * float(self.price)
    
#function returns data fron text in list(array)
def readStateFile(nameoffile):
    arrdata = []
    with open(nameoffile,'r') as f:
        textfile = f.readlines()
        if textfile == None:
            print("Error, empty file, try another one")
            return False
        else:
            for i in range(0, len(textfile)):
                textline = textfile[i].split(',', 2)
                arrline = Record()
                arrline.quantity = textline[0]
                arrline.data = textline[1]
                arrline.price = textline[2]
                arrdata.append(arrline)
            print("the file has been read without any problems")
            return arrdata

#check the order by date        
def checkOrderByDate(arrdata):
    previousdate = 0.0
    for i in range(0, len(arrdata)):
        if float(arrdata[i].data) < previousdate:
            print("array is not ordered by date")
            print("previousdate:", previousdate, "date:", arrdata[i].data) 
            return False
        previousdate = float(arrdata[i].data)
    return True

# sorting by time btw
def SortByDate(strings):
    sorted_strings = sorted(strings, key=lambda line: float(line.data))
    return sorted_strings

#how much is not taxed
def SellWithoutTax(arrdata, price):
    sum = 0.0
    for i in range(0, len(arrdata)):
        if (time.time() - float(arrdata[i].data)) >= SEC_IN_YEAR or float(arrdata[i].price) <= price:
            sum += float(arrdata[i].quantity)
    return sum

#counting benefit 
def Benefit(sum, price, arrdata):
    cantsell = sum
    hadpaid = 0.0
    taxable = 0.0
    for i in range(0, len(arrdata)):
        if float(sum) == 0.0:
            break
        else:
            if float(arrdata[i].quantity) >= cantsell:
                hadpaid += cantsell*float(arrdata[i].price)
                if (time.time() - float(arrdata[i].data)) <= SEC_IN_YEAR or float(arrdata[i].price) >= price:
                    taxable += cantsell*price
                cantsell = 0.0
                break
            else:
                hadpaid += arrdata[i].purchase_amount()
                if (time.time() - float(arrdata[i].data)) <= SEC_IN_YEAR or float(arrdata[i].price) >= price:
                    taxable += float(arrdata[i].quantity) * price
                cantsell -= float(arrdata[i].quantity)
    if cantsell != 0.0:
        print("insufficient funds, missing", cantsell, "BTC")
        return False
    else:
        print("had payed:", hadpaid)
        print("will get:", sum*price)    
        print("benefit:", sum*price - hadpaid)
        if taxable != 0.0:
            print("with tax:", taxable)
        return (sum*price - hadpaid), taxable
    
#add new line about the new purchase
def PurchaseNewLine(nameoffile):
    text = []
    print("number of coins:")
    text.append(input())
    text.append(str(time.time()))
    print("price:")
    text.append(input())
    with open(nameoffile,'a') as f:
        text = ", ".join(text)
        print(text)
        text = "\n" + text
        print(type(text))
        f.write(text)
        f.close()
    print("ok")

def SellDelLines(arrdata, price, nameoffile):
    print("how many had sold?")
    hadsold = float(input())
    text = []
    text.append(str(hadsold))
    text.append(str(price))
    text.append(str(Benefit(hadsold, price, arrdata)))
    for i in range(0, len(arrdata)):
        print("hadsold:", hadsold)
        if hadsold > 0.0:
            quant = float(arrdata[i].quantity)
            arrdata[i].quantity = float(arrdata[i].quantity) - hadsold
            hadsold -= quant
            if float(arrdata[i].quantity) <= 0.0:
                arrdata.pop(i)
        else:
            break
    if hadsold > 0:
        print("Error, not enough BTC")
        return False
    else:
        with open("saleshistory.txt", 'a') as f:
            text = ', '.join(text)
            text += '\n'
            f.write(text)
        f.close()
        print("add line in saleshistory.txt:", text)

        with open(nameoffile, 'w') as f:
            for i in range(0, len(arrdata)):
                textline = []
                textline.append(str(arrdata[i].quantity))
                textline.append(str(arrdata[i].data))
                textline.append(str(arrdata[i].price))
                textline = ','.join(textline)
                f.write(textline)
        f.close()
        