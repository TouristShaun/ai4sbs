import requests

def create_campaign(name, description, email_addresses):
    return requests.post(
        "https://api.marketo.com/v1/campaigns",
        json={
            "name": name,
            "description": description,
            "emailAddresses": email_addresses
        }
    )