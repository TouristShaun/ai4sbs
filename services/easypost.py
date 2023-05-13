import easypost
easypost.api_key = "your-api-key"

def create_shipment(to_address, from_address, parcel):
    to_address = easypost.Address(to_address)
    from_address = easypost.Address(from_address)
    parcel = easypost.Parcel(parcel)
    shipment = easypost.Shipment.create(to_address=to_address, from_address=from_address, parcel=parcel)
    return shipment