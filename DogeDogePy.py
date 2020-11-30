import bs4, requests
headers = {'User-Agent':
       'MAKE A GOOGLE SEARCH FOR MY USER AGENT AND PASTE IT HERE'}
search="test"
address='http://www.google.com/search?q='+search
res=requests.get(address,headers=headers)
soup=bs4.BeautifulSoup(res.text,'html.parser')
links=soup.select('div.r a')

l = [] #Empty list to display only the top 5 links

#Clean the soup by filtering only the information requested
for link in links:
  if "webcache.googleusercontent.com" in link.attrs["href"]:
    pass
  elif "#" in link.attrs["href"]:
    pass
  elif "/search?q=related:" in link.attrs["href"]:
    pass
  else:
    l.append(link.attrs["href"])

for i in range(5):
  print(l[i])
