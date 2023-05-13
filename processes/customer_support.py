from services import mailgun
def create_ticket(customer_id, subject, message):
    # Get the customer from the database
    customer = get_customer_from_db(customer_id)
    
    # Create a new ticket in the database
    ticket = create_ticket_in_db(customer_id, subject, message)
    
    # Send an email to the customer using Mailgun
    mailgun.send_email(customer.email, subject, message)
    
    return ticket