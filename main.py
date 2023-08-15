import time
import functions
import request

from tkinter import *  
from tkinter import scrolledtext 

# btc today in euro:
price = float(request.priceOfBTC())


while(1):
    print("press to:\n"
          "0 - exit\n"
          "1 - read new file\n"
          "2 - price\n"
          "3 - check order by date\n"
          "4 - sell without tax\n"
          "5 - benefit from selling X BTC\n"
          "6 - commit a new transaction\n"
          "7 - show file")
    i = int(input())
    if i == 0:
        break
    if i == 1:
        print("name of file:")
        filename = input()
        # the function converts text file into list form
        textlist = functions.readStateFile(filename)
    if i == 2:
        print("price of BTC right now:", price)
    if i == 3:
        if not functions.checkOrderByDate(textlist):
            print("list isn't sorted")
            print("if you want to sort list press 1, if not 0")
            if int(input()) != 0:
                textlist = functions.SortByDate(textlist)
            else:
                print("can't work with this file")
                break
        else:
           print("list is sorted")
    if i == 4:
        #counting sum that you can sell without tax
        print("Can sell withouy tax:", functions.SellWithoutTax(textlist, price))
    if i == 5:
        # count benefit
        print("how many want to sell?")
        sum = float(input())
        print(functions.Benefit(sum, price, textlist))
    if i == 6:
        print("if you bought BTC press 0, if sold - 1")
        if int(input()) == 0:
            functions.PurchaseNewLine(filename)
        else:
            functions.SellDelLines(textlist, price, filename)
    if i == 7: 
        with open(filename, 'r') as f:
            text = f.readlines()
        window = Tk()  
        window.title("Working file:")  
        window.geometry('400x250')  
        txt = scrolledtext.ScrolledText(window)  
        txt.grid(column=0, row=0)  
        txt.insert(INSERT, text)
        window.mainloop()
