import logging

logger = logging.getLogger(__name__)

def send_email(recipient, subject, body):
    try:
        # Code to send an email using Mailgun
        pass
    except Exception as e:
        logger.error(f"Error sending email:  {e}")