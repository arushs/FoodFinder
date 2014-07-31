import requests
import urllib
from bs4 import BeautifulSoup



requestURL = 'http://www.epicurious.com/tools/searchresults?search=bacon'
data = requests.get(requestURL)
file = urllib.urlopen(requestURL)
soup = BeautifulSoup(file)
imgs = soup.findAll("img", {"class":"sr_recipe_image"})
for img in imgs:
    # imgUrl = img.a['href'].split("imgurl=")[1]
    # urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))
    # start = img.find("src")
    # end = img.find("/>")
    # img[start:end]

    print(img.get("src"))
# print(soup.prettify())
