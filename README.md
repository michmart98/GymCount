# GymCount
This script fetches data from Google Calendar and calculates how many times you have gone to the gym within a specified time frame. It then uses the number of gym visits and a user-defined price per visit to calculate the total amount owed to the gym. 


## Functionality
This script fetches data from my calendar and calculates how much I should pay the gym based on the number of times I go. To achieve this, it does the following:

- Searches my Google Calendar for events named "Gym."
- Prompts me to enter the starting and ending dates that I want to be included in the timeline of my exercises for which I need to pay.
- Prompts me to enter the price per gym visit.
- If it finds an event in my calendar named "Gym paid", it means I have paid up to this date. Therefore, the script resets the counter and starts counting again after this date.


## Requirements
* Google client library for Python. Intall with: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
* pytz, to convert between timezones. Install with: pip install pytz
* Google Calendar API. You need credentials to your account to fetch the data. Check Google's instructions for this https://developers.google.com/calendar/api/quickstart/python
