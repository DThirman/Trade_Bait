import urllib
from StringIO import StringIO
import re

for i in range(1,1000):
    filehandle = urllib.urlopen('http://store.tcgplayer.com/magic/product/show?PageNumber='+str(i))
    print "read page " + str(i)
    lines = filehandle.readlines()
    line = reduce(lambda a,b: a + b, lines)

    p = re.compile(r'<a href="/magic/([\w-]*)/([\w-]*)"><img id="img_[\w-]*" src="([\w*:./]*)" onerror="this.src=\'http://i.tcgplayer.com/0.jpg\'" style="margin-bottom:5px;margin-top:5px"/></a>')
    m = p.findall(line)
    for card in m:
            downloaded_image = file(card[0]+"_"+card[1]+".jpg", "wb")
            image_on_web = urllib.urlopen(card[2])
            while True:
                    buf = image_on_web.read(65536)
                    if len(buf) == 0:
                            break
                    downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
    print "parsed page " + str(i)