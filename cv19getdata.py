#!/usr/bin/env python

##################################################################
#
# Python script to fetch data on COVID-19 cases in Indonesia
# from Google spreadsheet published in  http://kcov.id/daftarpositif
#
# Original data from the web was read, downloaded, and then saved as
# csv file for further processing / simulation
#
# This script uses Google API to read and fetch data from the spreadsheet.
# Original code was taken from:
# https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/
#


import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw'
SAMPLE_RANGE_NAME = 'Statistik Harian!A1:S30' # Example using sheet name : 'Class Data!A2:E'

def main():
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        print('No data found.')

main()

df=pd.DataFrame(values_input[1:], columns=values_input[0])

# Write the data into csv file
df.to_csv('daily.csv')
