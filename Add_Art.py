import os
import natsort
from os import listdir
from os.path import isfile, join
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient.http import MediaFileUpload

#Automatic authentication through saving credentials in a txt file for later use
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

mypath = "<YOUR PATH>"


#Confirmation and asking for amount of targeted users
add_art = input('Do you want to add 2 MRS to their folder? (y/n)\n>')
amount = input('For all users or only one specific? (f/l)\n>')


def singleuser():
    #gets list of paths of all files in targeted path
    onlyfiles = [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f]
    files = natsort.natsorted(onlyfiles,reverse=True)

    #gets ID of targeted drive folder
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folder_names = [names['title'] for names in file_list]
    position = folder_names.index(name)
    folder_id = [names['id'] for names in file_list]
    id = folder_id[position]
    #gets filenames of all files in targeted path
    file_list_1 = drive.ListFile({'q': f"'{id}' in parents and trashed=false"}).GetList()
    file_names = [names['title'] for names in file_list_1]

    onlyfiles1 = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    files1 = natsort.natsorted(onlyfiles1,reverse=True)

    ArtNr = 0
    success = 0
    Uploaded = 1

    filenr = f"file{Uploaded}"

    #If user wants to add files then upload 2 art in folder
    if add_art == 'y':
        #success < 2 is the amount of art that is being uploaded so for success < 3, 3 illustrations will be uploaded
        while success < 2:
            artpath = files[y]
            #if file isn't already in folder then upload said file, if it's already in folder, then target next file and check if it's in folder
            if files1[ArtNr] not in file_names:
                #set title and set in which folder the file will be created with 'id' then upload
                filenr = drive.CreateFile({'title': files1[ArtNr], 'parents': [{'id': [id]}]})
                filenr.SetContentFile(artpath)
                filenr.Upload()
                print(f"{Uploaded}. Illustration has been uploaded!")
                Uploaded = Uploaded + 1
                success = success + 1
            ArtNr = ArtNr + 1

    if success is 2:
        print("Finished uploading all illustrations!")

if amount == 'l':
    name = input('Enter name of user:\n>')
    singleuser()

if amount == 'f':
    print('Function has not been programmed yet.')
