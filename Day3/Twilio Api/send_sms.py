import schedule
import time

from twilio.rest import Client

from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

msg = "Good Morning Love! Hope You Have An Amazing Day <3"


def send_message():
    client = Client(twilio_account, twilio_token)
    client.messages.create(to=cellphone, from_=twilio_number, body=msg)


schedule.every().day.at("07:00").do(send_message, msg)

while True:
    schedule.run_pending()
    time.sleep(2)
