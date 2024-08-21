#===================================================================
#resconf-put.py
import ***
import ***
requests.packages.urllib3.disable_warnings()

api_url = "https://***/restconf/data/ietf-interfaces:interfaces/***"

headers = { "***": "***", 
            "***":"***"
           }

basicauth = ("***", "***")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "***",
        "description": "My *** RESTCONF loopback",
        "***": "iana-if-type:softwareLoopback",
        "enabled": ***,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "**.**.**.**",
                    "netmask": "**.**.**.**"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

#api request to send the PUT request


#conditional statement to check for returned response code

#end of file