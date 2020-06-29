from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

users = ['a', 'b', 'Liao']

def create_folder(users):
    folder_name = users
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
folder_names = [names['title'] for names in file_list]
#print(folder_names)

new_users = []
for names in users:
    if names not in folder_names:
        create_folder(names)
        new_users.append(names)

if new_users is not None:
    print(f'New supporters found! Users that have to be given access to: {new_users}')
else:
    print('No new supporters found.')
