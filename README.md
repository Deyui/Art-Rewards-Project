# Art Rewards Project
 Automating Patreon Rewards by utilizing the Patreon and Google Drive API with the PyDrive wrapper.
 Using the Patreon API to automatically get a list of all active Patrons. Pydrive matches these names from the list to all currently existing folders on the account and adds new folders if necessary (in case that new Patrons have joined). After creating the needed folders, it adds two new files, that fits each Patron's individual reward progressions, to it as well.
 Currently still WIP.
 
 # Requirements
 - Python 3+
 - `pip install patreon`
 - `pip install PyDrive`
 
 # Setup
 1. Install packages mentioned in Requirements
 
 2. Install [dependencies](https://github.com/Patreon/patreon-python/blob/master/setup.py#L12) from Patreon
 
 3. Retrieve your `Creator's Access Token` from Patreon [here](https://www.patreon.com/portal/registration/register-clients).  
      (We don't need the redirect URI so just enter a random valid URL)
      
 4. Follow this [documentation](https://pythonhosted.org/PyDrive/quickstart.html) or [video tutorial](https://www.youtube.com/watch?v=j31iVbkknzM) to set up PyDrive in order to get your Google Drive authenticated
 
 
 
 # Links
 Patreon API: https://github.com/Patreon/patreon-python    
 Patreon Dependencies: https://github.com/Patreon/patreon-python/blob/master/setup.py#L12  
 Patreon Clients & API Key: https://www.patreon.com/portal/registration/register-clients  
 PyDrive: https://github.com/gsuitedevs/PyDrive  
 PyDrive Documentation: https://pythonhosted.org/PyDrive/  
 PyDrive Setup YT Tutorial: https://www.youtube.com/watch?v=j31iVbkknzM  
 
