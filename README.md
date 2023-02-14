# GymCount
This is a script that fetch data from Google Calendar and counts how many times I hit the gym and how much should I pay.


## Functionality
I pay the gym according to the amount of times I go. 
This script fetch the data from my calendar and calcucate how much should I pay.
To do this: 
* It search in my Google Calendar event for events named "Gym"
* Gets as input the starting date and the ending date that I want to be included in the timeline of my exercises that I need to pay.
* Gets as input the price per visit to the gym.
* If it found an event in my calendar named "Gym paid", it means I have paid till this date. So it resets the counter, and starting counting again after this date.


## Requirements
* Google client library for Python. Intall with: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
* pytz, to convert between timezones. Install with: pip install pytz
* Google Calendar API. You need credentials to your account to fetch the data. Check Google's instructions for this https://developers.google.com/calendar/api/quickstart/python
