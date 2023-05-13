from services import stripe, hubspot

def create_order(customer_id, product_id, quantity):
    # Get the customer from the database
    customer = get_customer_from_db(customer_id)
    
    # Create a new order in the database
    order = create_order_in_db(customer_id, product_id, quantity)
    
    # Charge the customer's credit card using Stripe
    stripe.create_charge(customer.credit_card, order.total_price)
    
    # Create a new contact in HubSpot for this customer
    hubspot.create_contact(customer.email, customer.first_name, customer.last_name)
    
    return order