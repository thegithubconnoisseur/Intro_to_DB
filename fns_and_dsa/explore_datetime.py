from datetime import datetime, timedelta

def display_current_datetime():

    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {formatted}"
    


display_current_datetime()

days = int(input("Enter a number of days: "))

def calculate_future_date(days):
    
    current_date = datetime.now()

    future_date = current_date + timedelta(days = days)

    return f"Future date: {future_date.strftime("%Y-%m-%d")}"

calculate_future_date(days)
