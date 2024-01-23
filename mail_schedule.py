from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
def send_email():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\MM\\Downloads\\client_secret.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=credentials)

    emailmsg = 'This is msg using Gmail integration'
    mimemessage = MIMEMultipart()
    mimemessage['to'] = 'qaseemakhlaq786@gmail.com'
    mimemessage['subject'] = 'Gmail Integration'
    mimemessage.attach(MIMEText(emailmsg, 'plain'))

    raw_string = base64.urlsafe_b64encode(mimemessage.as_bytes()).decode('utf-8')
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)
send_email()
schedule.every().day.at("20:20").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
