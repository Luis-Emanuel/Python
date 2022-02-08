import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('ERRO!')
else:
    print('Tudo OK')