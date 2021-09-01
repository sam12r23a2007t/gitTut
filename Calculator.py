first_number=float(input("Enter the first number: "))
second_number=float(input("Enter the second number: "))
Operator=input("Enter operator: ")
if Operator=="+":
    print(f'The result is {first_number+second_number}')
elif Operator=="-":
    print(f'The result is {first_number-second_number}')
elif Operator=="*":
    print(f'The rsult is {first_number*second_number}')
elif Operator=="/":
    print(f'The result is {first_number/second_number}')
else:
    print("Wrong operator")