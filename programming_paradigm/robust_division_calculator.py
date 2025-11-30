def safe_divide(numerator, denominator):
    try:
        first = float(numerator)
        second = float(denominator)
        result = first/second

    except ZeroDivisionError:
        return"Error: Cannot divide by zero."
    
    except ValueError:
        return"Error: Please enter numeric values only."

    else:
        return f"The result of the division is {result}"