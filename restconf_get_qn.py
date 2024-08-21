#===================================================================
#resconf-get_qn.py
import ***
import ***
requests.packages.urllib3.disable_warnings()

api_url = "https://xx.xx.xx.xx/restconf/data/ietf-interfaces:interfaces"

headers = { "***": "***", 
            "***":"***"
           }

basicauth = ("***", "***")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=***)

print(resp)

response_json = resp.json()
print(json.dumps(***, ***))

#end of file

