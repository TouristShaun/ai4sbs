from services import google_sheets
def generate_report(report_type):
    # Generate the report from the database
    report = generate_report_from_db(report_type)
    
    # Upload the report to Google Sheets
    google_sheets.upload_report(report)
    
    return report