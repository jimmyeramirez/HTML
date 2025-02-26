
item1 = "eggs"
item2 = "milk"
item3 = "bread"
item4 = "cheese"
item5 = "lettuce"
item6 = "sugar"
item7 = "ham"
item8 = "turkey"
item9 = "water"
item10 = "bitcoin"
price1 = 5.99
price2 = 6.99
price3 = 3.99
price4 = 9.99
price5 =1.99
price6 = 2.99
price7 = 8.33
price8 = 5.50
price9 = 15.00
price10 = 100.99

#sub_total = sum(price1, price2, price3, price4, price5, price6, price7, price8, price9, price10)
#above cannt not be done because "sum" it self is an function so this formula is saying total of total, it would be different if you it was Sum(and the actual price)


sub_total = price1 + price2 + price3 + price3 + price4 + price5 + price6 + price7 + price8 + price10


print(sub_total)

print()


taxes = .09

total = sub_total + (sub_total * taxes)

tax_total= total * taxes

print(tax_total)
print()


print("the subtotal is:", sub_total)
print()


print("the total is:", total)
print()


print("the total paid in taxes is:", tax_total)










      