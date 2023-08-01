import time
import functions
#i btc today in euro:
price = 26444
sum, firsttax = functions.SellWithoutTax()

print(functions.Benefit(sum,firsttax,price))

functions.AddLine()