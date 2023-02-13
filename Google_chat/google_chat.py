# Send message to google chat using webhook done:
from json import dumps
from collections import namedtuple

from httplib2 import Http
from pathlib import Path

def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAAdk0RfP4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=PJlz1jlkF_sTwv6NrIOAhyLSXn3tNHRo_WuXVczzPC0%3D" and "https://chat.googleapis.com/v1/spaces/AAAA-bhBOGo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=hF2P8nCahOjnnjRTWwdrIQWxcRQOINPIEAowg6pLscY%3D"
    txt = Path('/home/dhruvish.p@ah.zymrinc.com/Documents/csrf').read_text()
    bot_message = {
        'text': txt}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    Status_display = list(response)   
    if int(Status_display[0]["status"]) == 200:
        print("Success")
    else:
        print("Fail")

if __name__ == '__main__':
    main()


# ******************************************************************************************************


# Create chat message(Have some error due to requried google workspace account:)

# from apiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# import pickle
# import datefinder
# from datetime import datetime, timedelta

# scopes = ['https://www.googleapis.com/auth/chat.messages.create']
# flow = InstalledAppFlow.from_client_secrets_file("/home/dhruvish.p@ah.zymrinc.com/Downloads/client_secret_488899379378-uvklro0n84302n6k3j8i6p7vjjtr2bht.apps.googleusercontent.com.json", scopes=scopes)
# credentials = flow.run_console()
# pickle.dump(credentials, open("token.pkl", "wb"))
# credentials = pickle.load(open("token.pkl", "rb"))
# service = build("chat", "v1", credentials=credentials)

# def create_message():
#     return service.spaces().messages().create(

#     # The space to create the message in.
#     #
#     # Replace SPACE with a space name.
#     # Obtain the space name from the spaces resource of Chat API,
#     # or from a space's URL.
#     parent='spaces/Chat_connection',

#     # The message to create.
#     body=
#     {
#       'cardsV2': [{
#         'cardId': 'createCardMessage',
#         'card': {
#           'header': {
#             'title': 'A Card Message!',
#             'subtitle': 'Created with Chat REST API',
#             'imageUrl': 'https://developers.google.com/chat/images/chat-product-icon.png',
#             'imageType': 'CIRCLE'
#           },
#           'sections': [
#             {
#               'widgets': [
#                 {
#                   'buttonList': {
#                     'buttons': [
#                       {
#                         'text': 'Read the docs!',
#                         'onClick': {
#                           'openLink': {
#                             'url': 'https://developers.google.com/chat'
#                           }
#                         }
#                       }
#                     ]
#                   }
#                 }
#               ]
#             }
#           ]
#         }
#       }]
#     }

# ).execute()

# create_message()



# ******************************************************************************************************



# Run api on client secret:

# from apiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow

# scopes = ['https://www.googleapis.com/auth/chat.spaces']

# flow = InstalledAppFlow.from_client_secrets_file("/home/dhruvish.p@ah.zymrinc.com/Downloads/client_secret2.json", scopes=scopes)
# flow.run_console()