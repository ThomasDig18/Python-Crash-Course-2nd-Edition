guest_list = ['naruto', 'sasuke', 'sakura', 'kakashi']

guest_list.remove('sakura')


print(f'{guest_list[0].title()} Want to come to dinner?')
print(f'{guest_list[1].title()} Want to come to dinner?')
print(f'{guest_list[2].title()} Want to come to dinner?')

print('I have found a bigger table actually')

guest_list.insert(0, 'Jarayia')
guest_list.insert(2, 'Tsunade')
guest_list.append('Gaara')

print(f'{guest_list[0].title()} Want to come to dinner?')
print(f'{guest_list[1].title()} Want to come to dinner?')
print(f'{guest_list[2].title()} Want to come to dinner?')
print(f'{guest_list[3].title()} Want to come to dinner?')
print(f'{guest_list[4].title()} Want to come to dinner?')
print(f'{guest_list[5].title()} Want to come to dinner?')

guest_list.pop()
guest_list.pop()
guest_list.pop()

print(f'invite {guest_list} out to dinner')
