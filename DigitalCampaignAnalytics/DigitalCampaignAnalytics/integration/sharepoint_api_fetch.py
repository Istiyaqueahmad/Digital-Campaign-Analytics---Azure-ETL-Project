
import requests

url = "https://yourtenant.sharepoint.com/_api/web/lists/getbytitle('CampaignData')/items"
headers = {
    "Accept": "application/json;odata=verbose",
    "Authorization": "Bearer <access_token>"
}

response = requests.get(url, headers=headers)
data = response.json()

# Print sample campaign names
for item in data['d']['results']:
    print(item['Title'])
