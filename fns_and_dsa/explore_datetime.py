from datetime import datetime, timedelta

def display_current_datetime():

    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted
    #return f"Current date and time: {formatted}"
    


apple = display_current_datetime()
print(f"Current date and time: {apple}")


days = int(input("Enter a number of days: "))

def calculate_future_date(days):
    
    current_date = datetime.now()

    future_date = current_date + timedelta(days = days)
    return future_date
    #eturn f"Future date: {future_date.strftime("%Y-%m-%d")}"

pear = calculate_future_date(days)
print(f"Future date: {pear.strftime("%Y-%m-%d")}")