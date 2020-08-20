#4-10

pizza_toppings = ["pepperoni", "sausage", "bacon", "chicken", "ranch"]
print("The first three items in the list are: ")
for toppings in pizza_toppings[0:3]:
	print(toppings) 

#4-11

friends_toppings = pizza_toppings[:]


pizza_toppings.append("anchovies")

friends_toppings.append("pineapple")







print("My favorite toppings are: ")
print(pizza_toppings)

print("My friends favorite toppings are: ")
print(friends_toppings)
