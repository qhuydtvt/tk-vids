from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import re



def search(search_terms):
    SEARCH_FORMAT = "http://www.nhaccuatui.com/tim-kiem?q={}"
    search_terms = quote_plus(search_terms.strip().lower())
    url = SEARCH_FORMAT.format(search_terms)
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    ul_song_list = soup.find('ul', 'search_returns_list')
    li_first_song = ul_song_list.find('li')
    a_song_link = ul_song_list.find('a', 'name_song search')
    return a_song_link["href"]


def extract_song_source(song_link):
    html = urlopen(song_link).read().decode('utf-8')
    re_xml = re.compile("file=(.*?)\"")
    xml_match = re_xml.search(html)
    xml_link = xml_match.group().replace('file=', '').replace('\"', '')
    song_xml = urlopen(xml_link).read().decode('utf-8')

    import xmltodict
    song_xml_dict = xmltodict.parse(song_xml)

    location = song_xml_dict["tracklist"]["track"]["location"]
    location = location.replace('<![CDATA[','').replace(']]>', '')
    return location


def get_song_source(search_terms):
    link = search(search_terms)
    return extract_song_source(link)


if __name__ == "__main__":
    link = get_song_source("angle with a shotgun nightcore")
    print(link)
