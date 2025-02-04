import requests

response = requests.get("https://api.github.com/repos/keneojiteli/deimos-sre-tasks/commits") #this is a request object and is not iterale
extracted_response = response.json() # parse or extract the body, this part is iterable
print(type(extracted_response))

for res in range(len(extracted_response)):
    print(extracted_response[res]["commit"]["message"])

