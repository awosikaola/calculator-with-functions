def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print ('Hello Please Select An Option')

print ('1.Add')
print ('2.Subtract')
print ('3.Multiply')
print ('4.Divide')

while True:
    choice = input('Enter an option from 1-4: ')

    if choice in ('1', '2', '3', '4'):
        n1 = float(input('Enter First Number: '))
        n2 = float(input('Enter Second Number: '))

        if choice == '1':
            print(n1, '+', n2, '=', add(n1,n2))

        elif choice == '2':
            print(n1, '-', n2, '=', sub(n1,n2))

        elif choice == '3':
            print(n1, '*', n2, '=', mul(n1,n2))

        elif choice == '4':
            print(n1, '/', n2, '=', div(n1,n2))

        break

    else:
        print ('Invalid Imput')