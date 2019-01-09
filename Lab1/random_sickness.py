from gmail import GMail, Message

sickness_list = ["Máu trắng", "HIV",]

#template
#https://html5-editor.net/
text = '''
<p>Ch&agrave;o sếp</p>
<p>H&ocirc;m nay em đi kh&aacute;m b&aacute;c sỹ bảo em bị <strong>{{sickness}}</strong></p>
<p>N&ecirc;n em xin ph&eacute;p sếp cho em nghỉ ng&agrave;y h&ocirc;m nay</p>
<p>Em c&aacute;m ơn sếp</p>
<p>Nh&acirc;n vi&ecirc;n</p>
'''     

#hàm choice của thư viện random

import random

sickness = random.choice(sickness_list)
html_content = html.replace("{{sickness}}", sickness)#.replace()  #content


gmail = GMail('B.User <nhungnguyen.tedx@gmail.com>','rocket.89p13')
msg = Message('Test Message',to='Huy <qhuydtvt@gmail.com>', html = text)
gmail.send(msg)

