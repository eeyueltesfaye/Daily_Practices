#  Handling ZeroDivisionError

def divide_numbers():
    try:
        numerator = float(input("Enter the first number (numerator): "))
        denominator = float(input("Enter the second number (denominator): "))
        
        result = numerator / denominator
        
        print(f"The result of {numerator} divided by {denominator} is {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")

divide_numbers()



