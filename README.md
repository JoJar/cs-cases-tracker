# cs-cases-tracker

https://developers.google.com/sheets/api/quickstart/python

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Code to update google sheet document containing case information. This application updates the current price in the spreadsheet with the realtime prices at runtime.

TODO:
Track case price history.

requirements: 
- Python 3.10.7 or greater
- The pip package management tool
- A Google Cloud project.
- A Google Account.

to run:
- enter directory
- add your spreadsheet_id to the sheetsUpdateValues (['YOUR_SPREADSHEET_ID'])*
- python3 sheetsUpdateValues


* Spreadsheet ID is found after /d/ in your spreadsheet url: 'https://docs.google.com/spreadsheets/d/'YOUR_SPREADSHEET_ID'/
