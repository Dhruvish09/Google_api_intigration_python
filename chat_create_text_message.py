from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

# Specify required scopes.
SCOPES = ['https://www.googleapis.com/auth/chat.spaces']

# Specify service account details.
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    '/home/dhruvish.p@ah.zymrinc.com/Downloads/dhruv-chat.json', SCOPES)

# Build the URI and authenticate with the service account.
chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

# Create a Chat message.
res = chat.spaces().list().execute()
print("res:",res)
result = chat.spaces().messages().create(

    # The space to create the message in.
    #
    # Replace SPACE with a space name.
    # Obtain the space name from the spaces resource of Chat API,
    # or from a space's URL.
    parent='spaces/Chat_connection',

    # The message to create.
    # body={'text': 'Hello, world!'}

    body=
    {
      'cardsV2': [{
        'cardId': 'createCardMessage',
        'card': {
          'header': {
            'title': 'A Card Message!',
            'subtitle': 'Created with Chat REST API',
            'imageUrl': 'https://developers.google.com/chat/images/chat-product-icon.png',
            'imageType': 'CIRCLE'
          },
          'sections': [
            {
              'widgets': [
                {
                  'buttonList': {
                    'buttons': [
                      {
                        'text': 'Read the docs!',
                        'onClick': {
                          'openLink': {
                            'url': 'https://developers.google.com/chat'
                          }
                        }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
      }]
    }

).execute()

print(result)
