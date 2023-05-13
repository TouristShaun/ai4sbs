from services import easypost
def fulfill_order(order_id):
    # Get the order from the database
    order = get_order_from_db(order_id)
    
    # Fulfill the order using Easypost
    easypost.fulfill_order(order)
    
    return order