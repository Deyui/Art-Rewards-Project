from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Get your GDrive Account authenticated
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


#Preexisting folders, that you want the user to have access to
Folder_1 = drive.CreateFile({'id': [ID]})
Folder_2 = drive.CreateFile({'id': [ID]})

Folder_1.Upload()
Folder_2.Upload()

#All Folders that are in this list will be getting access permission
all_folders = [Folder_1, Folder_2]

#function that iterates through list and gives each access permission
def access(email):
    address = email
    for folders in all_folders:
        folders.InsertPermission({'type': 'user',
                                                 'value': address,
                                                 'role': 'reader'})

#in case a new folder has to be created, function that creates a folder that will then be pushed to all_folders
def create_folder(name):
    folder_name = name
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    all_folders.append(folder)


#asking for E-mail that will be getting the access as well as whether new folder needs to be created
new = input('Should a folder be created for the user? (y/n)\n>')
email = input('Enter E-mail Address:\n>')

#If no new folder needs to be created, access permission will be sent to the E-mail address for the folders in "all_folders"
if new == 'n':
    access(email)
elif new == 'y':
    # If new folder has to be created, name of said folder will be asked, then created through the create_folder function
    name = input('Enter new supporter name:\n>')
    create_folder(name)
    print('Created folder!')
    access(email)
    print('Success!')
