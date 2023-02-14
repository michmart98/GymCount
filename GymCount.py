from __future__ import print_function

import pytz
import datetime
import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
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

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Get the calendar events in a particular timeline
        calendar_id = "primary" # Replace with the ID of your calendar
        time_min_str = input("Enter the start time in the format 'DD-MM-YYYY': ")
        time_max_str = input("Enter the end time in the format 'DD-MM-YYYY': ")
        # I want it to be in Europe/Athens time
        athens_tz = pytz.timezone('Europe/Athens')
        time_min = datetime.datetime.strptime(time_min_str, '%d-%m-%Y').replace(tzinfo=pytz.utc).astimezone(athens_tz).strftime('%Y-%m-%dT00:00:00Z')
        time_max = datetime.datetime.strptime(time_max_str, '%d-%m-%Y').replace(tzinfo=pytz.utc).astimezone(athens_tz).strftime('%Y-%m-%dT23:59:59Z')
        events_result = service.events().list(calendarId=calendar_id, timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy="startTime").execute()
        events = events_result.get("items", [])

        # Count the number of occurrences of the gym event
        gym_count = 0
        for event in events:
            if event["summary"] == "Gym":
                gym_count += 1

        # Calculate the total amount to be paid for the gym
        gym_fee_per_visit = int(input("Price of visit to the gym: "))
        gym_pay = gym_count * gym_fee_per_visit

        # Print the results
        print(f"You went to the gym {gym_count} times")
        print(f"You should pay a total of {gym_pay} € for your gym visits")

        if not events:
            print('No events found.')
            return

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()