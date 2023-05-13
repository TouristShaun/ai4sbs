import requests

def create_contact(email, first_name, last_name):
    return requests.post(
        "https://api.hubspot.com/contacts/v1/contact/",
        headers={"Content-Type": "application/json"},
        json={
            "properties": [
                {"name": "email", "value": email},
                {"name": "firstname", "value": first_name},
                {"name": "lastname", "value": last_name}
            ]
        }
    )