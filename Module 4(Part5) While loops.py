user_name = 'python'
password = 'rules'
num_try = 5
while num_try > 0:
    name = input('Enter user name: ')
    pas = input('Enter password: ')
    if name == user_name and pas == password:
        print('Welcome!')
        break
    num_try = num_try -1
else:
    print('Access denied')
