import mlab
from bike_rental import Bike

mlab.connect()

f= Bike(model="Yamaha Grande",dailyfee="40000000",image="https://image-us.24h.com.vn/upload/1-2018/images/2018-01-26/1516929124-839-yamaha-grande-o-viet-nam-gay-sot-thi-truong-nuoc-ngoai-ya1-1516922772-width660height440.jpg",year="2016")
f.save()