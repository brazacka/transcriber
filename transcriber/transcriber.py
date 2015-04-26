import eyed3
import urllib2
from bs4 import BeautifulSoup

def update_version(filename, version = (2,3,0)):
    song = eyed3.load(filename)
    song.tag.version = version
    song.tag.save()

def set_comment(filename, text, desc=u'Transcriber'):
    if check_version(filename) == (2,2,0):
        print "Updating to version 2.3.0"
        update_version(filename)
    song = eyed3.load(filename)
    song.tag.comments.set(text, desc)
    song.tag.save()

def check_version(filename):
    song = eyed3.load(filename)
    return song.tag.version

def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()

def get_song_title(filename):
    song = eyed3.load(filename)
    title = song.tag.title
    return title

def get_song_artist(filename):
    song = eyed3.load(filename)
    artist = song.tag.artist
    return artist

def get_tabs_url(filename):
    url = 'http://www.911tabs.com/tabs'
    artist = get_song_artist(filename)
    title = get_song_title(filename)
    url += '/' + artist[0].lower()
    url += '/' + artist.lower().replace(' ', '_')
    url += '/' + title.lower().replace(' ', '_')
    url += '.htm'
    return url

def make_soup(html):
    return BeautifulSoup(html)

def get_top_tab_url(filename):
    url = get_tabs_url(filename)
    html = get_html(url)
    soup = make_soup(html)
    return soup.select('.b-table_song > .b-table-bg > .line a')[0]['data-url']

def get_tab(filename):
    # This currently only works with GuitareTab
    url = get_top_tab_url(filename)
    html = get_html(url)
    soup = make_soup(html)
    tab_element = soup.select('pre')[0]
    dumb_tags = tab_element.find_all('a')
    for tag in dumb_tags:
        tag.replace_with(str(tag.contents))
    return tab_element

def write_tab(filename):
    tab = unicode(get_tab(filename))
    set_comment(filename, tab)

