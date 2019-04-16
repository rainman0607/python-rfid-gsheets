import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
# Get the downloaded credentials from oAuth
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', url)

# Authorize request
gc = gspread.authorize(creds)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Test").sheet1
