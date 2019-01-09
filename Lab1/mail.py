from gmail import GMail, Message

t = '''
<p><span style="color: #00ff00;"><span style="text-decoration: underline;">Someone</span> in the crowd&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></span></p>
<h4><strong>could be the one&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-surprised.gif" alt="surprised" /></strong></h4>
<p>you need<em> <img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" />&nbsp;to know</em></p>
'''
gmail = GMail('B.User <nhungnguyen.tedx@gmail.com>','rocket.89p13')
msg = Message('Test Message',to='Huy <qhuydtvt@gmail.com>', html = t)
gmail.send(msg)