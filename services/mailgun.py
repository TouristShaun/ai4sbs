import requests

def send_email(to, subject, text):
    return requests.post(
        "https://api.mailgun.net/v3/your-domain.com/messages",
        auth=("api", "your-api-key"),
        data={"from": "Excited User <mailgun@your-domain.com>",
                "to": [to],
                "subject": subject,
                "text": text})