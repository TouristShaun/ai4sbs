import stripe

stripe.api_key = "your-api-key"

def create_charge(amount, currency, card_number, card_expiry_month, card_expiry_year, card_cvc):
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        card={
            "number": card_number,
            "expiry_month": card_expiry_month,
            "expiry_year": card_expiry_year,
            "cvc": card_cvc
        }
    )