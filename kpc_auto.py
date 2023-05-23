import requests

requrl = 'https://kyc-api.aadhaarkyc.io/api/v1/bank-verification/'
header = { "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MjQ2OTg2NSwianRpIjoiMTFhODJhYTYtZjFlYS00NjZlLWJmYjMtYjdlMmQ2MjU0YjA0IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LnplbmNvbkBzdXJlcGFzcy5pbyIsIm5iZiI6MTY3MjQ2OTg2NSwiZXhwIjoxOTg3ODI5ODY1LCJ1c2VyX2NsYWltcyI6eyJzY29wZXMiOlsid2FsbGV0Il19fQ.jhAEXOX6YXP6LS_EyhwplkPYRlf26XP5W28WX91mRlY"}

body = {
	"id_number": "003901561845",
	"ifsc": "ICIC0000039",
    "ifsc_details": True
}
response = requests.request("POST", requrl, headers=header, data=body)

print(response.text)