from services import stripe
def create_invoice(customer_id, order_id):
    # Get the customer and order from the database
    customer = get_customer_from_db(customer_id)
    order = get_order_from_db(order_id)
    
    # Create a new invoice in the database
    invoice = create_invoice_in_db(customer_id, order_id)
    
    # Charge the customer's credit card using Stripe
    stripe.create_charge(customer.credit_card, invoice.total_price)
    
    return invoice