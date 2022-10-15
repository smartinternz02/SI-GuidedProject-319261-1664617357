import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "iMzFyOH5ywPwzGz5KMCL8Hi9sPlV98EhvNuDLG9HHoxO"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18","f19","f20","f21","f22","f23","f24","f25","f26","f27","f28","f29","f30","f31","f32","f33","f34","f35","f36","f37","f38","f39"]], "values":[[0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1, 29.85, 29.85]] }]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b9d3ebbc-c106-4941-9c05-98dd4ae32fe0/predictions?version=2022-10-14', json=payload_scoring,
 headers= {'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred= response_scoring.json()
output=pred['predictions'][0]['values'][0][0]
print(output)
