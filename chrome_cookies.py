import browser_cookie3
from pickle import dump

chromeCookies  = browser_cookie3.chrome(domain_name='.economist.com')

filename = "cookies.pkl"

Cookies={}

for cookie in chromeCookies:
    Cookies[cookie.name]=cookie.value

with open(filename, 'wb') as file:
    dump(Cookies, file)