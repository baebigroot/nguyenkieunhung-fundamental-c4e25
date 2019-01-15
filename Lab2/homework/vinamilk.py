from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

f = open("vinamilk.html", "wb") 
f.write(raw_data)
f.close()

soup = BeautifulSoup(content,"html.parser")
table = soup.find("table",id="tableContent")
data = []

for row in table.find_all("tr"):
    for cell in row.find_all("td"): 
        cell = cell.string
        figure = OrderedDict({
            "": cell,
        })
        data.append(figure)

pyexcel.save_as(records=data, dest_file_name="vinamilk.xlsx")

