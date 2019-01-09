from gmail import GMail, Message

sickness_list = ["máu trắng", "HIV", "mọc răng khôn"]

text = '''
<p>Ch&agrave;o sếp</p>
<p>H&ocirc;m nay em đi kh&aacute;m b&aacute;c sỹ bảo em bị <strong>{{sickness}}</strong></p>
<p>N&ecirc;n em xin ph&eacute;p sếp cho em nghỉ ng&agrave;y h&ocirc;m nay</p>
<p>Em c&aacute;m ơn sếp</p>
<p>Nh&acirc;n vi&ecirc;n</p>
'''     

import datetime
now = datetime.datetime.now()

import random
sickness = random.choice(sickness_list)
html_content = text.replace("{{sickness}}", sickness)

run_once = 0

while run_once == 0:
    if now.hour == 7:
        gmail = GMail('B.User <nhungnguyen.tedx@gmail.com>','rocket.89p13')
        msg = Message('Test Message',to='Nhung <kieunhung1229@gmail.com>', html = html_content)
        gmail.send(msg)
        run_once += 1




