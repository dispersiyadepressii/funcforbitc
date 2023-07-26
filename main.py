import time
import functions
import request
# btc today in euro:
price = float(request.PriceOfBitc())
sum, firsttax = functions.SellWithoutTax()

print(functions.Benefit(sum,firsttax,price))

functions.AddLine()



