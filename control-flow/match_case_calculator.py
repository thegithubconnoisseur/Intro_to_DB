

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:

        case "+":
            addition = num1 + num2
            print(f"The result is {addition}.")
            break
        
        case "-":
            subtraction = num1 - num2
            print(f"The result is {subtraction}.")
            break

        case "*":
            multiplication = num1 * num2
            print(f"The result is {multiplication}.")
            break

        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                break
            
            else:
                division = num1/ num2
                print(f"The result is {division}.")
                break
        
        case _:
            print("Enter one of the arithmetics provided in the question above")
