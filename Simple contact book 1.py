# simple contact book 
#copyright of this code have Abdirizak abdullahi hussein 
print('SIMPLE CONTACT BOOK')
print()
print('1.Add contact')

User = input()

if User == '1':
	print()
	name = input('Enter contact name: ')
	phone = input('Enter contact phone number: ')
	print()
	print('Name = ', name)
	print('Phone = ', phone)

Con = False

while Con == False:
	print('SIMPLE CONTACT BOOK')
	print()
	print('1.Add contact')
	print('2.search contact')
	print('0.Exit')
	User = input()
	if User == '1':
		print()
		name = input('Enter contact name: ')
		phone = input('Enter contact phone number: ')
		name.strip()
		phone.strip()
		print()
		print('Name = ', name)
		print('Phone = ', phone)
		
	elif User == '2':
			sear = input('Enter contact number or name: ')
			if sear == name or sear == phone:
				print('Name:', name)
				print('Phone: ', phone)
			else:
				print('No contact found!')
	elif User == '0':
		Con = True
	else:
		continue
		
