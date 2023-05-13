from services import eventbrite
def create_event(name, description, start_time, end_time):
    # Create a new event in the database
    event = create_event_in_db(name, description, start_time, end_time)
    
    # Create a new event in Eventbrite
    eventbrite.create_event(event)
    
    return event