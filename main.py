import time
import functions
import request
# btc today in euro:
price = float(request.PriceOfBitc())
nameoffile = 'new_register.txt'

sum, firsttax = functions.SellWithoutTax()

print(functions.Benefit(sum,firsttax,price))

functions.AddLine()



