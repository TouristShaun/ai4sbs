from services import marketo
def create_campaign(name, description, email_list):
    # Create a new campaign in the database
    campaign = create_campaign_in_db(name, description)
    
    # Send the campaign to the email list using Marketo
    marketo.send_campaign(campaign.id, email_list)
    
    return campaign