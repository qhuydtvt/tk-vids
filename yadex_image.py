from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

def get_img_source(search_terms):
    search_terms = quote_plus(search_terms.strip().lower())
    SEARCH_FORMAT = "https://yandex.com/images/search?text={0}&isize=medium&type=photo"
    url = SEARCH_FORMAT.format(search_terms)
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    get_img_source("how long charlie puth")
