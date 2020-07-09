from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Get your GDrive Account automatically authenticated
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

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

add_art = input('Do you want to add 3 MRS to their folder? (y/n)\n>')

mypath = "<YOUR PATH>"

onlyfiles = [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f]
files = natsort.natsorted(onlyfiles,reverse=True)


file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
folder_names = [names['title'] for names in file_list]
position = folder_names.index(name)
folder_id = [names['id'] for names in file_list]
id = folder_id[position]
file_list_1 = drive.ListFile({'q': f"'{id}' in parents and trashed=false"}).GetList()
file_names = [names['title'] for names in file_list_1]
#print(file_names)

onlyfiles1 = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files1 = natsort.natsorted(onlyfiles1,reverse=True)
#print(files)

y = 0
x = 0
z = 1

filenr = f"file{z}"

if add_art == 'y':
    while x < 3:
        artpath = files[y]
        if files1[y] not in file_names:
            filenr = drive.CreateFile({'title': files1[y], 'parents': [{'id': [id]}]})
            filenr.SetContentFile(artpath)
            filenr.Upload()
            print(f"{z}. Illustration has been uploaded!")
            z = z + 1
            x = x + 1
        y = y + 1

if x is 3:
    print("Finished uploading all illustrations!")
