import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def get_folder_id(service, folder_name):
    results = service.files().list(q=f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false",
                                   pageSize=1000).execute()
    folders = results.get('files', [])
    
    if not folders:
        print(f'Folder "{folder_name}" not found in your Google Drive.')
        return None

    return folders[0]['id']

def is_file_in_folder(service, file_id, folder_id):
    file = service.files().get(fileId=file_id, fields='parents').execute()
    if folder_id in file.get('parents', []):
        return True
    return False

def move_files_to_folder(service, folder_id):
    results = service.files().list(q="trashed=false and 'root' in parents", pageSize=1000).execute()
    files = results.get('files', [])

    if not files:
        print('No files found in the root directory of your Google Drive.')
        return

    for file in files:
        file_id = file['id']
        file_name = file['name']
        
        print(f'Moving {file_name}...')
        
        # Check if the file is already in the "FILES" folder
        if not is_file_in_folder(service, file_id, folder_id):
            try:
                # Move the file to the "FILES" folder by setting the parents field
                service.files().update(fileId=file_id, addParents=folder_id).execute()
            except Exception as e:
                print(f'Error occurred while moving {file_name}: {e}')
        else:
            print(f'{file_name} is already in the "FILES" folder. Skipping.')

    print('All files moved to "FILES" folder successfully.')

def main():
    credentials = authenticate()
    service = build('drive', 'v3', credentials=credentials)

    # Replace 'FILES' with the actual folder name if different
    folder_name = 'FILES'
    folder_id = get_folder_id(service, folder_name)

    if folder_id is None:
        return

    move_files_to_folder(service, folder_id)

if __name__ == '__main__':
    main()
