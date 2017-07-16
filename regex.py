__author__ = 'joseph'

import re
import urllib

try:
    import urllib.request
except ImportError:
    pass

sites = 'beeg'.split()

for s in sites:
    print('Searching: ' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except AttributeError:
        u = urllib.request.urlopen('http://' + s + '.com')
    print(u.read())
    text = u.read()
    title = re.findall(r'<title>+.*</title>+', str(text), re.I|re.M)

    # print(title[0])

