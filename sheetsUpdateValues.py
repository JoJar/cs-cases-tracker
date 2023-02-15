from __future__ import print_function

import google.auth
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import getData as getData
from time import sleep

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def sheets_batch_update(spreadsheet_id, newData, row_start, row_end, column_start, column_end):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    # pylint: disable=maybe-no-member

    try:
        service = build('sheets', 'v4', credentials=creds)

        requests = []
        # Find and replace text
        requests.append({
            "repeatCell": 
                {
                    "cell": 
                        {
                            "userEnteredFormat": 
                                {
                                    "horizontalAlignment": "CENTER",
                                    "textFormat": 
                                        { "bold":True }
                                },
                            "userEnteredValue":
                                {
                                    "numberValue":newData
                                },
                            "effectiveValue":
                                {
                                    "stringValue":"1234"
                                }

                        },


                    
                        "range": 
                            {
                                "sheetId": 0,
                                "startRowIndex": row_start,
                                "endRowIndex": row_end,
                                "startColumnIndex": column_start,
                                "endColumnIndex": column_end
                            },
                        "fields":"userEnteredValue"
                }
        })

        body = {
            'requests': requests
        }

        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()
        return response

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.cs20(), 1, 2, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.clutch(), 2, 3, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.dangerZone(), 3, 4, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.fracture(), 4, 5, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.gamma2(), 5, 6, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.horizon(), 6, 7, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.snakebite(), 7, 8, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.vanguard(), 8, 9, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.brokenFang(), 9, 10, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.prisma(), 10, 11, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.prisma2(), 11, 12, 4, 5)
    sleep(0.2)
    sheets_batch_update('1-Dd8K81BaWF0TseXJqYFj1lRqjkQ8dd0MVB1IwYBdp0', getData.stockholmChampAutograph(), 12, 13, 4, 5)
    sleep(0.2)
    