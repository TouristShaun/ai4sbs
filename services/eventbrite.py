import requests

def create_event(name, description, start_time, end_time, location):
    return requests.post(
        "https://www.eventbrite.com/api/v3/events",
        headers={"Content-Type": "application/json"},
        json={
            "name": name,
            "description": description,
            "start_time": start_time,
            "end_time": end_time,
            "location": location
        }
    )