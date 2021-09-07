import random

yes_no_dict = {'yes': True, 'no': False}

print('Enter the number of friends joining (including you):')
number_of_friends = int(input())
if number_of_friends < 1:
    print('No one is joining for the party')
    exit()

payments = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(number_of_friends):
    name = input()
    payments[name] = 0

print('Enter the total bill value:')
bill = float(input())

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
somebody_is_lucky = yes_no_dict[input().lower()]
lucky_name = ''
if somebody_is_lucky:
    lucky_name = random.choice(list(payments.keys()))
    print(lucky_name, 'is the lucky one!')
else:
    print('No one is going to be lucky')


bill_for_each = round(bill / (number_of_friends - int(somebody_is_lucky)), 2)

for p in payments.keys():
    payments[p] = bill_for_each

if somebody_is_lucky:
    payments[lucky_name] = 0

print(payments)