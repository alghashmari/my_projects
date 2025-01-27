import requests
from datetime import datetime


USER_NAME = "alghashmari"
TOKEN = "fldsakfkldsajfkdjfls"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id":  GRAPH_ID,
    "name": "Studying",
    "unit": "Hour",
    "type": "float",
    "color": "sora"
}
headers ={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today = datetime.now()
DATE = today.strftime("%Y%m%d")
post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_config = {
    "date": DATE,
    "quantity": input("How many hours did i study today"),
}
response = requests.post(url=post_endpoint,json=post_config,headers=headers)
print(response.text)

pix_update_endpoint = f"{post_endpoint}/{DATE}"
pix_update_config = {
    "quantity":"7"
}
# response = requests.put(url=pix_update_endpoint, json=pix_update_config, headers=headers)
# print(response.text)