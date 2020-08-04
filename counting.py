numbers = list(range(1, 1000000))
#4-4   4-5
print(min(numbers))

print(max(numbers))

print(sum(numbers))
#4-6
odd_numbers = list(range(1, 20, 2))

print(odd_numbers)

for number in odd_numbers:
	print(number)

#4-7
multiples_3 = list(range(3, 30, 3))

for numbers in multiples_3:
	print(numbers)

#4-8
cubes = []
for numbers in range(1, 10):
		cubes.append(numbers**3)


print(cubes)

#4-9
cubes_1 = [x**3 for x in range(1,10)]
print(cubes_1)