foods = ["Hamburger", "Fries", "Chicken Fried"]
price =[30,20,15]
resibo = []
grandTotal = 0
run = True

while run :
    for k in range (len(foods)):
        print(k,"-",foods[k], price[k])


    order = int(input("What is your order? :"))
    if order == 5:
         break
    else:
        quantity = int(input("how many po?:"))
        grandTotal += price[order]*quantity
        ris = (str(foods[order]), str(price[order]), str(quantity))
        resibo.append(ris)

for k in resibo:
    print(k)
print("total:",grandTotal)






