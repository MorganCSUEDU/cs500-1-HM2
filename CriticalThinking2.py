//Task #1
def calculate_restaurant_bill():
    # Input the charge for the food
    food_charge = float(input("Enter your food bill: $"))

    # Calculate the tip (20% because that seems to be the minimum these days, SMH)
    tip = food_charge * 0.20

    # Calculate the sales tax (9% Washington State Sales Tax)
    sales_tax = food_charge * 0.09

    # Calculate the total bill
    total_bill = food_charge + tip + sales_tax

    # Display the amounts
    print(f"Food Charge: ${food_charge:.2f}")
    print(f"Tip (20%): ${tip:.2f}")
    print(f"Sales Tax (9%): ${sales_tax:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")

calculate_restaurant_bill()

//Task #2
import time
from datetime import datetime

def calculate_alarm_time():
    # Offer the user the option to use the current time or enter their own time
    use_current_time = input("Do you want to use the current time? (y/n): ")

    if use_current_time.lower() == 'y':
        current_time = datetime.now().strftime("%H:%M")
        print(f"Current time: {current_time}")
    else:
        current_time = input("Enter the current time (in the format HH:MM): ")

    # Extract hours and minutes from the input
    current_hour, current_minute = map(int, current_time.split(":"))

    # Convert current time to hours
    current_time_hours = current_hour + current_minute / 60

    # Input the number of hours to wait for the alarm
    wait_time = float(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the alarm time in hours
    alarm_time_hours = (current_time_hours + wait_time) % 24

    # Convert the alarm time back to the format "HH:MM"
    alarm_hour = int(alarm_time_hours)
    alarm_minute = int((alarm_time_hours - alarm_hour) * 60)
    print(f"The alarm is set for {alarm_hour:02d}:{alarm_minute:02d}")

    # Calculate the total waiting time in seconds
    total_wait_seconds = int(wait_time * 3600)

    # Countdown to the alarm time
    for remaining_seconds in range(total_wait_seconds, 0, -1):
        hours, seconds = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        time_format = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"Time remaining: {time_format}", end='\r')
        time.sleep(1)

    print("\nWake up! It's alarm time!")

calculate_alarm_time()
