import gspreadsheets
from google.auth.credentials import ServiceAccountCredentials

def create_spreadsheet(name, sheet_names):
    creds = ServiceAccountCredentials.from_file('your-service-account.json')
    client = gspreadsheets.Client(creds)
    spreadsheet = client.create(spreadsheet=name, shout='true')
    for name in sheet_names:
        spreadsheet.add_worksheet(name=name, rows=10, cols=10)
    return spreadsheet