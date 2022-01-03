from bs4 import BeautifulSoup
from requests import get
from random import randint
import webbrowser

if __name__ == "__main__":

    links = []

    x = input("search >> ").replace(' ','+')

    url = "https://www.google.com/search?q=" + x + "&sxsrf=AOaemvI7eXD4dcvbbBTOzkQJ_hpZiHToZQ:1641232810046&source=lnms&tbm=isch&sa=X&ved=2ahUKEwign4vVlJb1AhWAAxAIHV9tAWwQ_AUoAXoECAEQAw&biw=1458&bih=794&dpr=1.25"

    page = get(url)

    bs = BeautifulSoup(page.text, 'html.parser')

    for div in bs.find_all('img'):
        link = div['src']
        if 'https://' in link:
            links.append(link)

    webbrowser.open(links[randint(0, len(links))])