FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return float(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return float(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


tempis = input("Enter the temperature to convert: ")
scale = input("Is this temperature in Celsius or Fahrenheit? (choose C or F): ")

# match scale:
#     case 'C':
#         work_done = convert_to_fahrenheit(tempis)
#         print(f"{tempis}°C is {work_done}°F")
#     case 'F':
#         work_done = convert_to_celsius(tempis)
#         print(f"{tempis}°F is {work_done}°C")
#     case _:
#         raise ValueError("Invalid temperature. Please enter a numeric value.")

if scale == 'C':
    work_done = convert_to_fahrenheit(tempis)
    print(f"{float(tempis)}°C is {work_done}°F")
elif scale == 'F':
    work_done = convert_to_celsius(tempis)
    print(f"{float(tempis)}°F is {work_done}°C")
else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
