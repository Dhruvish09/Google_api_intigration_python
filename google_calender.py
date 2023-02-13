# Create google calender meeting:

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datefinder
from datetime import datetime, timedelta

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("/home/dhruvish.p@ah.zymrinc.com/Downloads/client_secret_488899379378-uvklro0n84302n6k3j8i6p7vjjtr2bht.apps.googleusercontent.com.json", scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
# result = service.calendarList().list().execute()
# print("result['items'][0]:",result['items'])


def create_event(start_time_str, summary, duration=1, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    
    event = {
        'summary': 'Google chat- Sprint retrospection',
        'location': 'Mondeal Heights, A/1402, Sarkhej - Gandhinagar Hwy, Ramdev Nagar, Ahmedabad, Gujarat 380015',
        'description': 'A chance to hear more about Google\'s developer products.',
        'htmlLink': 'https://zymr.zoom.us/j/4404961316?pwd=bE9ETnJBMHc5eVk3Z3lvbXpJZ0JHQT09',
        'colorId': 5,
        'status': 'confirmed',
        'transparency': 'opaque',
        'visibility': 'private',
        'attachments': [
        {
            'fileUrl': 'https://drive.google.com/file/d/17so2l6bGdyEESVPLUPqhidqTJv9ICYIe/view',
            'title': 'Invitation for developer session'
        }
    ],
        # "creator": {
        #     "id": "234",
        #     "email": "pateldhruvish612000@gmail.com",
        #     "displayName": "Dhruvish Patel",
        #     "self": True
        #     },
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
            ],
        # 'attendees': [
        #     {
        #         'email': {'prince.makavana@zymr.com','naveen.pandia@zymr.com','darshit.shah@zymr.com'},
        #     # {
        #         # {'email': 'prince.makavana@zymr.com'},
        #         # {'email': 'naveen.pandia@zymr.com'},
        #     # },
        #         'displayName': 'Dhruvish Patel',
        #         'comment': "Let's learn something new in developement side",
        #         'optional': False,
        #         'organizer': True,
        #         'responseStatus': 'accepted',
        #     }
        # ],
        'attendees': [
            {'email': 'prince.makavana@zymr.com'},
            {'email': 'naveen.pandia@zymr.com'},
            ],

        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        "eventType": "Testing in google calender"
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()
    
create_event("15 feb 1 PM", "Meeting")

# ******************************************************************************************
# Another way of create calender event  using python

# from Google import Create_Service,convert_to_RFC_datetime
# from datetime import datetime
# import datefinder
# from datetime import datetime, timedelta

# CLIENT_SECRET_FILE =  '/home/dhruvish.p@ah.zymrinc.com/Downloads/client_secret_488899379378-uvklro0n84302n6k3j8i6p7vjjtr2bht.apps.googleusercontent.com.json'
# API_NAME = 'calendar'
# API_VERSION = 'v3'
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# calendar_id_india = '5ff47f9d7eb28bd35c3ffc012989011c1093d5e9d2015999ca2c1310cbce015f@group.calendar.google.com'

# # Create_event:

# # colors = service.colors().get().execute()
# # hour_adjustment = -8
# # now = datetime.now()

# def create_event(start_time_str, duration=1, description=None, location=None):
#     matches = list(datefinder.find_dates(start_time_str))
#     if len(matches):
#         start_time = matches[0]
#         end_time = start_time + timedelta(hours=duration)

#     event = {
#         'start':
#         {
#             'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#             'timeZone': 'Asia/Kolkata',
#         },
#         'end':
#         {
#             'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#             'timeZone': 'Asia/Kolkata',
#         },

#         # 'start': {
#         #     'dateTime': now.strftime("%Y-%m-%dT%H:%M:%S"),
#         #     'timeZone': 'Asia/Kolkata',
#         # },
#         # 'end': {
#         #     'dateTime': now.strftime("%Y-%m-%dT%H:%M:%S"),
#         #     'timeZone': 'Asia/Kolkata',
#         # },
#         'summary': 'Family Lunch',
#         'description': 'Having lunch with the parents',
#         'colorId': 5,
#         'status': 'confirmed',
#         'transparency': 'opaque',
#         'visibility': 'private',
#         'location': 'Mondeal Heights, A/1402, Sarkhej - Gandhinagar Hwy, Ramdev Nagar, Ahmedabad, Gujarat 380015',
#         'attachments': [
#             {
#                 'fileUrl': 'https://drive.google.com/file/d/17so2l6bGdyEESVPLUPqhidqTJv9ICYIe/view',
#                 'title': 'Invitation for developer session'
#             }
#         ],

#         # "gadget": {
#         #     "type": 'object',
#         #     "title": 'Go To Website',
#         #     "link": 'https://url',
#         #     "iconLink": 'https://icon-url',
#         #     "width": 100,
#         #     "height": 100,
#         #     "display": 'chip'
#         # },
#         # 'attendees': [
#         #     {
#         #     'email': ['prince.makavana@zymr.com'],
#         #     'email': ['naveen.pandia@zymr.com'],
#         #     # 'email': {'prince.makavana@zymr.com','naveen.pandia@zymr.com','darshit.shah@zymr.com'},
#         #         # {
#         #             # {'email': 'prince.makavana@zymr.com'},
#         #             # {'email': 'naveen.pandia@zymr.com'},
#         #         # },
#         #     'displayName': 'Dhruvish Patel',
#         #     'comment': "Let's learn something new in developement side",
#         #     'optional': False,
#         #     'organizer': True,
#         #     'responseStatus': 'accepted',
#         #     }
#         # ],
#         'reminders': {
#             'useDefault': False,
#             'overrides': [
#             {'method': 'email', 'minutes': 24 * 60},
#             {'method': 'popup', 'minutes': 10},
#             ],
#         },

#         'attendees': 
#         [
#             {'email': 'prince.makavana@zymr.com'},
#             {'email': 'naveen.pandia@zymr.com'},
#         ],
#             'displayName': 'Dhruvish Patel',
#             'comment': "Let's learn something new in developement side",
#             'optional': False,
#             'organizer': True,
#             'responseStatus': 'accepted',
#     }
#     # maxAttendees = 5
#     # sendNotification = True
#     # sendUpdate = 'none'
#     # supportsAttachments = True

#     return service.events().insert(
#         calendarId = calendar_id_india,
#         maxAttendees = 5,
#         sendNotifications=True,
#         sendUpdates='none',
#         supportsAttachments=True,
#         body = event,

#     ).execute()

# create_event("15 feb 1 PM")
#     # print("#################response",response)


# # ***********************************************************
#     # (1)Get list of calendar:-
#     # get_list = service.calendarList().list().execute()

#     # (2)Delete calendar:-
#     # service.events().delete(calendarId='primary', eventId='eventId').execute()

#     # (3)Update calendar:-
#     # event = service.events().get(calendarId='primary', eventId='eventId').execute()

#     # event['summary'] = 'Appointment at Somewhere'

#     # updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

#     # Print the updated date.
#     # print updated_event['updated']


#     # (4)Change calendar date:-
#     # updated_event = service.events().move(
#     # calendarId='primary', eventId='eventId',
#     # destination='destinationCalendarId').execute()

#     # Print the updated date.
#     # print updated_event['updated']
# # ***********************************************************