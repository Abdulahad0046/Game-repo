print("CALCULATOR")
first_number = int(input("enter a number: "))
second_number = int(input("enter a number: "))
operator = input("enter the operator (+,-,*,/): ")
try:
    if operator == "+":
        print(first_number+second_number)
    elif operator == "-":
        print(first_number-second_number)
    elif operator == "*":
        print(first_number*second_number)
    elif operator == "/":
        print(first_number/second_number)
    else:
        print("Invalid task")
finally:
    print("Thankyou for using our calculator....")