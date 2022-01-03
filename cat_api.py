import requests
import webbrowser

if __name__ == '__main__':
    response = requests.get('https://api.thecatapi.com/v1/images/search')

    results = (response.json())[0]

    url_photo = results['url']
    width_photo = results['width']
    height_photo = results['height']

    webbrowser.open(url_photo)