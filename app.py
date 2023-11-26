 # Edit this One AI API call using our studio at https://studio.oneai.com/?pipeline=llu0ZY&share=true

 import requests
 api_key = 
 url = "https://api.oneai.com/api/v0/pipeline"
 user_input = input("Write a prompt: ")
 headers = {
   "api-key": api_key, 
   "content-type": "application/json"
 }
 payload = {
   "input": user_input,
   "input_type": "article",
 	"output_type": "json",
   "multilingual": {
     "enabled": True
   },
   "steps": [
     {
       "skill": "gpt"
     }
   ],
 }

# r = requests.post(url, json=payload, headers=headers)
# data = r.json()
# print(data['text'])
# Edit this One AI API call using our studio at https://studio.oneai.com/?pipeline=llu0ZY&share=true

import requests
import json
api_key = "2120de50-8e64-4b34-95c5-00d1cb206cea"
url = "https://api.oneai.com/api/v0/pipeline"
user_input = input("Write a prompt: ")
headers = {
  "api-key": api_key, 
  "content-type": "application/json"
}
payload = {
  "input": user_input,
  "input_type": "article",
	"output_type": "json",
  "multilingual": {
    "enabled": True
  },
  "steps": [
    {
      "skill": "gpt"
    }
  ],
}

r = requests.post(url, json=payload, headers=headers)

data = r.json()

print(data)
