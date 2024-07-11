#input product prices from the user
#until total price exeeds 1000
#print the average price of the products
#print how many products you have purchased
#print how much beyond 1000 you reached
#('you went 500 beyond 1000')
total = 0
products = 0
while total <= 1000:
    price: float = float(input("What's the product's price?"));
    total = total+price;
    products = products+1
avg = total/products
dif = total-1000
print (f"you bought {products} products for the total sum of {total}.\nIn doing so you went {dif} beyond 1000, with an average price of {avg}")