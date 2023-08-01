import time
import functions
import request

# btc today in euro:
price = float(request.priceOfBTC())

# filename (temporarily, working in the program
#with only one file)
filename = 'register_copi.txt'
# the function converts text file into list form
textlist = functions.readStateFile(filename)

if functions.checkOrderByDate(textlist) == 1:
    textlist = functions.SortByDate(textlist)
    print(textlist)

#counting sum that you can sell without tax
print(functions.SellWithoutTax(textlist))

# count benefit
print("how many want to sell?")
sum = float(input())
print(functions.Benefit(sum, price, textlist))

#functions.AddLine()



