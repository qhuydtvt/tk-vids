from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import re



def search(search_terms):
    SEARCH_FORMAT = "http://www.nhaccuatui.com/tim-kiem/bai-hat?q={0}"
    search_terms = quote_plus(search_terms.strip().lower())
    url = SEARCH_FORMAT.format(search_terms)
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    ul_song_list = soup.find('ul', 'search_returns_list')
    if ul_song_list is None:
        return None

    li_first_song = ul_song_list.find('li', 'list_song search')
    if li_first_song is None:
        return None

    a_song_link = li_first_song.find('a')
    if a_song_link is None:
        return None

    return a_song_link["href"]


def extract_song_source(song_link):
    html = urlopen(song_link).read().decode('utf-8')
    re_xml = re.compile("file=(.*?)\"")
    xml_match = re_xml.search(html)
    xml_group = xml_match.group()
    if xml_group is None:
        return None
    xml_link = xml_group.replace('file=', '').replace('\"', '')
    song_xml = urlopen(xml_link).read().decode('utf-8')

    import xmltodict
    song_xml_dict = xmltodict.parse(song_xml)

    location = song_xml_dict["tracklist"]["track"]["location"]
    location = location.replace('<![CDATA[','').replace(']]>', '')
    return location


def get_song_source(search_terms):
    link = search(search_terms)
    if link is None:
        return None
    return extract_song_source(link)


if __name__ == "__main__":
    link = get_song_source("dança do creu mc créu")
    print(link)
