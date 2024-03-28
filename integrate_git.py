from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
#creating a flask application instance
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    
#fill your url
    url = "<fill info>.atlassian.net//rest/api/3/issue"
#fill your info
    auth = HTTPBasicAuth("<youremail>", "<yourapi")

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "fields": {
       "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Order entry fails when selecting supplier.",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "issuetype": {
          "id": "10006"
        },

        "project": {
          "key": "GS"
        },
        "summary": "First jira ticket",

        },

      "update": {}
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))



app.run('0.0.0.0', port = 5000)
