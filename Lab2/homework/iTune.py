from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#PART 1
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

f = open("iTune.html", "wb") 
f.write(raw_data)
f.close()

soup = BeautifulSoup(content, "html.parser")

section_chart = soup.find("section", "section chart-grid")

li_list = section_chart.find_all("li")
song_chart = []
for li in li_list:
    h4 = li.h4 #h4 của li
    a = h4.a
    # print(a)
    ordinal = li.strong.string
    song = li.h3.a.string
    artist = li.h4.a.string
    chart = OrderedDict({
        "Ordinal": ordinal,
        "Song": song,
        "Artist": artist
    })
    song_chart.append(chart)


pyexcel.save_as(records=song_chart, dest_file_name="iTune.xls")

#PART 2
from youtube_dl import YoutubeDL
options = {
    "default_search": "ytsearch",
    "max_downlaod": 1
}
dl = YoutubeDL(options)
dl.download([song + artist])
