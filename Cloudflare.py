import json
import requests

domain_name = 
zone = 
API_KEY = 
myIP = requests.get("https://ifconfig.me/ip").content


# set headers
header_info = {
	"content-type":"application/json",
	"Authorization":"Bearer " + API_KEY
}


# API request to get zone id
r = requests.get("https://api.cloudflare.com/client/v4/zones?name=" + zone, headers=header_info)
x = json.loads(r.content)
zone_id = x['result'][0]['id']


# API request to get record identifier
r = requests.get("https://api.cloudflare.com/client/v4/zones/" + zone_id + "/dns_records", headers=header_info)
records = json.loads(r.content)['result']
for record in records:
	if record['name'] == domain_name:
		record_id = record['id']

# request to update record
payload = {
	"type":"A",
	"name":domain_name,
	"ttl": 1,
	"content": myIP
}

p = requests.put("https://api.cloudflare.com/client/v4/zones/"  + zone_id  + "/dns_records/" + record_id, data=json.dumps(payload), headers=header_info)
print(p.content)
