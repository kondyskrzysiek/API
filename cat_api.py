# import requests module]
import requests
import webbrowser

# Making a get request
response = requests.get('https://api.thecatapi.com/v1/images/search')
results = (response.json())[0]['url']
webbrowser.open(results)
