balance = 10000
choice = input('Deposit or Withdraw: ')
amount = int(input('Amount of money: '))

if choice == 'Deposit':
    balance += amount
    print(f'Balance: {balance}')
if choice == 'Withdraw':
    balance -= amount
    if balance < 0:
        print("Ther aren't enough balance in your account!")
    else:
        print(f'Balance: {balance}')