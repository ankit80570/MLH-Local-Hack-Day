import sendgrid
import schedule
import time
from apikey import key

sg = sendgrid.SendGridAPIClient(api_key=key)
data = {
    "personalizations": [
        {
            "to": [
                {
                    "email": "ankXXXXXX@gmail.com"
                }
            ],
            "subject": "Sending with SendGrid is Fun"
        }
    ],
    "from": {
        "email": "ankit.XXXXX@student.XXXX.edu"
    },
    "content": [
        {
            "type": "text/plain",
            "value": "Good Morning Love! Hope You Have An Amazing Day <3"
        }
    ]
}


def send_email():
    response = sg.client.mail.send.post(request_body=data)


schedule.every().day.at("07:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(2)
