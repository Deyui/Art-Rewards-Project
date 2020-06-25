#get the Patreon API in the script
import patreon

#verify client with token
access_token = '<Your Token>'
api_client = patreon.API(access_token)

#Get the API to get information from 'campaign'
campaign_response = api_client.fetch_campaign()

#From that information we want the first item's id
campaign_id = campaign_response.data()[0].id()

#creating list where all patrons' information  will be stored
all_pledges = []

#cursor tells us if there are any pages left to paginate for us to know that we have to search through to get all patron names
#if cursor = none, then there are no pages left
cursor = None

#printing a sentence to check if script is working properly until now since fetching all data might take some time
print("Fetching Patron names...")

#looping cursor until we have paginated all pages and thus have fetched all patron names
while True:
    pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor, fields = {'pledge': ['declined_since']})
    all_pledges += pledges_response.data()
    cursor = api_client.extract_cursor(pledges_response)

    #breaking out of loop when cursor = none, when there are no pages left
    if not cursor:
        break

#creating list where all patrons' full names are stored
all_patrons = [patrons.relationship('patron').attribute('full_name') for patrons in all_pledges]


#removing all patrons that have been declined
not_declined = []

for patrons in all_pledges:
    declined = (patrons.attribute('declined_since'))

    if not declined:
        not_declined.append({
        'full_name': patrons.relationship('patron').attribute('full_name')
        })

#removing blank spaces at the end as well as remove VIPs that do not need to be on the list
active_patrons = [patrons['full_name'] for patrons in not_declined]
formatted = [names.rstrip() for names in active_patrons]

VIP = ['<Exceptions>']
formatted = [ele for ele in formatted if ele not in VIP]

print(formatted)
