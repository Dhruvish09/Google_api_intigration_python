from Google import Create_Service

CLIENT_SECRET_FILE =  '/home/dhruvish.p@ah.zymrinc.com/Downloads/client_secret1.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def create_folder_drive():
    national_parks = ['Yellowstone', 'Rocky Mountain', 'Yosemite']

    for national_park in national_parks:
        file_metadata = {
            'name': national_park,
            'mimeType': 'application/vnd.google-apps.folder'
        }
    return service.files().create(body=file_metadata).execute()


create_folder_drive()