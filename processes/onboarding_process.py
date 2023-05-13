from services import hubispot, mailgun
def onboard_customer(customer_id):
    # Get the customer from the database
    customer = get_customer_from_db(customer_id)
    
    # Create a new contact in HubSpot for this customer
    hubispot.create_contact(customer.email, customer.first_name, customer.last_name)
    
    # Send a welcome email to the customer using Mailgun
    mailgun.send_email(customer.email, "Welcome to our service!", "Hello "+customer.first_name+", we're glad to have you as a customer.")