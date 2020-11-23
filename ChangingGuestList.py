dinner_guests = ['mom', 'dad', 'brother', 'sister', 'pippin']
for guest in dinner_guests: 
	print(f"Do you want to come to dinner, {dinner_guests.pop()}")

print(f"{dinner_guests[1]} can't make it ")

cannot_make = dinner_guests.pop(1)
print(f"{cannot_make} can't make it")

dinner_guests.insert(1, 'Jones')

print(f'Do you want to come now that dad cannot, {dinner_guests[1]}?')

