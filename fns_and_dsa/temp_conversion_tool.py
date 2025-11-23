FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


tempis = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (choose C or F): ")

match scale:
    case 'C':
        work_done = convert_to_fahrenheit(tempis)
        print(f"{tempis}°C is {work_done}°F")
    case 'F':
        work_done = convert_to_celsius(tempis)
        print(f"{tempis}°F is {work_done}°C")