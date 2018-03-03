#!/usr/bin/env python
import urllib
class recent(object):
    def __init__(self, show=1):
        url = "https://forum.ubuntu-tr.net/index.php?action=recent"
        socket = urllib.urlopen(url)
        self.source = socket.readlines()
        self.show = show
    def read(self, id=0):
        for test in self.source:
            search = '<div class="list_posts">'
            if test.find(search) is not -1:
                if self.show < 1:
                    print "Hatali id!"
                    exit()
                else:
                    id = id +1
                    if id is self.show:
                        start = test.find(search) + len(search) 
                        end = test.find('</div>', start)
                        break
        return test[start:end]
post = recent(1)
print post.read()
