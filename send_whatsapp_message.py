import os
import schedule
import time
from twilio.rest import Client
from datetime import datetime

# Twilio credentials (replace with your own in a secure way, like environment variables)
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_whatsapp_number"

# List of recipients in order
schedule_order = [
    ("Vyshakh", "+1234567890"),
    ("Adhan", "+1234567891"),
    ("Amal Funda", "+1234567892"),
    ("Jopaul", "+1234567893"),
    ("Govind", "+1234567894"),
    ("Moota", "+1234567895"),
    ("Kenz", "+1234567896"),
    ("Delu Babz", "+1234567897")
]

# Determine the next person in the schedule
start_date = datetime(2025, 3, 20)  # Start date of rotation
cycle_length = len(schedule_order)

def get_recipient_message():
    days_since_start = (datetime.now() - start_date).days
    weeks_since_start = days_since_start // 7
    index = weeks_since_start % cycle_length
    recipient_name, recipient_number = schedule_order[index]
    return recipient_name, recipient_number

def send_message(message_text):
    recipient_name, recipient_number = get_recipient_message()
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
        body=message_text.replace("{name}", recipient_name),
        to=f"whatsapp:{recipient_number}"
    )
    
    print(f"Message sent to {recipient_name} ({recipient_number}): {message_text}")

# Scheduling messages
schedule.every().wednesday.at("23:00").do(send_message, "Did you put the bins out?")
schedule.every().thursday.at("23:00").do(send_message, "Hey {name}, this is your garbage week. Please don't forget to manage the garbage this week.")

# Keep running the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
