# 1. Write a Python program to test if a given page is found or not on the server. 
import csv
from bs4 import BeautifulSoup
from lxml import html
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://abcxyz.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print(html.read())
    
try:
    html = urlopen("http://www.example.com/")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("HTML Details")    
    print(html.read())  

# 2. Write a Python program to download and display the content of robot.txt for en.wikipedia.org. 
import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text
print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(test)

# 3. Write a Python program to get the number of datasets currently listed on data.gov.
response = requests.get('http://www.data.gov/')
doc_gov = html.fromstring(response.text)
link_gov = doc_gov.cssselect('small a')[0]
print("Number of datasets currently listed on data.gov:")
print(link_gov.text)

# 4. Write a Python program to convert an address(like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates(like latitude 37.423021 and longitude - 122.083739). 
# Geocodin: Geocoding is the process of converting addresses(like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates(like latitude 37.423021 and longitude - 122.083739), which you can use to place markers on a map, or position the map.
geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
my_address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India',
              'language': 'en'}
response = requests.get(geo_url, params=my_address)
results = response.json()['results']
my_geo = results[0]['geometry']['location']
print("Longitude:", my_geo['lng'], "\n", "Latitude:", my_geo['lat'])

# 5. Write a Python program to display the name of the most recently added dataset on data.gov. 
from lxml import html
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
doc = html.fromstring(response.text)
title = doc.cssselect('h3.dataset-heading')[0].text_content()
print("The name of the most recently added dataset on data.gov:")
print(title.strip())

# 6. Write a Python program to extract h1 tag from example.com.
html = urlopen('http://www.example.com/')
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh.h1)

# 7. Write a Python program to extract and display all the header tags from en.wikipedia.org/wiki/Main_Page. 
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')

# 8. Write a Python program to extract and display all the image links from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer). 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')

# 9. Write a Python program to get 90 days of visits broken down by browser for all sites on data.gov. 
r = requests.get("https://analytics.usa.gov/data/live/browsers.json")
print("90 days of visits broken down by browser for all sites:")
print(r.json()['totals']['browser'])

# 10. Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page. 
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
  if 'href' in link.attrs:
    print(link.attrs['href'])

# 11. Write a Python program to check whether a page contains a title or not. 
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
    
    title = getTitle(url)
    if title == None:
      return "Title could not be found"
    else:
      return title

print(getTitle("https://www.w3resource.com/"))
print(getTitle("http://www.example.com/"))

# 12. Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org. 
html = urlopen('https://www.wikipedia.org/')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.findAll('a', {'class': 'link-box'})
for name in nameList:
  print(name.get_text())


# 13. Write a Python program to get the number of people visiting a U.S. government website right now. 
# Source: https: // analytics.usa.gov/data/live/realtime.json
#https://bit.ly/2lVhlLX
# via: https://analytics.usa.gov/
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print("Number of people visiting a U.S. government website-")
print("Active Users Right Now:")
print(j['data'][0]['active_visitors'])


# 14. Write a Python program get the number of security alerts issued by US-CERT in the current year. 
# Source: https: // www.us-cert.gov/ncas/alerts
#https://bit.ly/2lVhlLX
url = 'https://www.us-cert.gov/ncas/alerts'
doc = html.fromstring(requests.get(url).text)
print("The number of security alerts issued by US-CERT in the current year:")
print(len(doc.cssselect('.item-list li')))

# 15. Write a Python program to get the number of Pinterest accounts maintained by U.S. State Department embassies and missions. 
# Source: https: // www.state.gov/r/pa/ode/socialmedia/
#https://bit.ly/2lVhlLX
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect(
    'a') if 'pinterest.com' in str(a.attrib.get('href'))]
print("The number of Pinterest accounts maintained by U.S. State Department embassies and missions:")
print(len(pinlinks))

# 16. Write a Python program to get the number of followers of a given twitter account. 
handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'lxml')
try:
    follow_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))
except:
    print('Account name not found...')


# 17. Write a Python program to get the number of following on Twitter. 

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'lxml')

try:
    following_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("{} is following {} people.".format(
        handle, following.get('data-count')))

except:
    print('Account name not found...')

# 18. Write a Python program to get the number of post on Twitter liked by a given account. 

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'lxml')

try:
    favorite_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find(
        'span', {'class': 'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(
        handle, favorite.get('data-count')))

except:
    print('Account name not found...')

# 19. Write a Python program to count number of tweets by a given Twitter account. 

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'lxml')

try:
    tweet_box = bs.find(
        'li', {'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets = tweet_box.find('a').find('span', {'class': 'ProfileNav-value'})
    print("{} tweets {} number of tweets.".format(
        handle, tweets.get('data-count')))

except:
    print('Account name not found...')

# 20. Write a Python program to scrap number of tweets of a given Twitter account. 
from bs4 import BeautifulSoup
import requests
handle = input('Input your account name on Twitter: ')
ctr = int(input('Input number of tweets to scrape: '))
res=requests.get('https://twitter.com/'+ handle)
bs=BeautifulSoup(res.content,'lxml')
all_tweets = bs.find_all('div',{'class':'tweet'})
if all_tweets:
  for tweet in all_tweets[:ctr]:
    context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
    content = tweet.find('div',{'class':'content'})
    header = content.find('div',{'class':'stream-item-header'})
    user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
    time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
    message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
    footer = content.find('div',{'class':'stream-item-footer'})
    stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
    if context:
      print(context)
    print(user,time)
    print(message)
    print(stat)
    print()
else:
    print("List is empty/account name not found.")
  
# 21. Write a Python program to find the live weather report(temperature, wind speed, description and weather) of a given city. 
import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=****************************8&units=metric');
	return res.json();
def print_weather(result,city):
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
def main():
	city=input('Enter the city:')
	print()
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
if __name__=='__main__':
	main()

# 22. Write a Python program to display the date, days, title, city, country of next 25 Hackevents. 
import requests
from bs4  import BeautifulSoup
res = requests.get('https://hackevents.co/hackathons')
bs = BeautifulSoup(res.text, 'lxml')
hacks_data = bs.find_all('div',{'class':'hackathon '})
for i,f in enumerate(hacks_data,1):
    hacks_month = f.find('div',{'class':'date'}).find('div',{'class':'date-month'}).text.strip()
    hacks_date = f.find('div',{'class':'date'}).find('div',{'class':'date-day-number'}).text.strip()
    hacks_days = f.find('div',{'class':'date'}).find('div',{'class':'date-week-days'}).text.strip()
    hacks_final_date = "{} {}, {} ".format(hacks_date, hacks_month, hacks_days )
    hacks_name = f.find('div',{'class':'info'}).find('h2').text.strip()
    hacks_city = f.find('div',{'class':'info'}).find('p').find('span',{'class':'city'}).text.strip()
    hacks_country = f.find('div',{'class':'info'}).find('p').find('span',{'class':'country'}).text.strip()
    print("{:<5}{:<15}: {:<90}: {}, {}\n ".format(str(i)+')',hacks_final_date, hacks_name.title(), hacks_city, hacks_country))
  

# 23. Write a Python program to download IMDB's Top 250 data(movie name, Initial release, director name and stars). 
#https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])
  
# 24. Write a Python program to get movie name, year and a brief summary of the top 10 random movies. 
from bs4 import BeautifulSoup
import requests
import random
def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies
def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()

def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url

def imd_movie_picker():
    ctr=0
    print("--------------------------------------------")
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        print(movie_title, movie_year)
        print(movie_summary)
        print("--------------------------------------------")
        ctr=ctr+1
        if (ctr==10):
          break;   
if __name__ == '__main__':
    imd_movie_picker()
  
# 25. Write a Python program to get the number of magnitude 4.5 + earthquakes detected worldwide by the USGS.
#https://bit.ly/2lVhlLX
# landing page:
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
csvurl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
rows = list(csv.DictReader(requests.get(csvurl).text.splitlines()))
print("The number of magnitude 4.5+ earthquakes detected worldwide by the USGS:", len(rows))


# 26. Write a Python program to display the contains of different attributes like different attributes like status_code, headers, url, history, encoding, reason, cookies, elapsed, request and content of a specified resource. 
response = requests.get('https://python.org')
print("Status Code: ", response.status_code)
print("Headers: ", response.headers)
print("Url: ", response.url)
print("History: ", response.history)
print("Encoding: ", response.encoding)
print("Reason: ", response.reason)
print("Cookies: ", response.cookies)
print("Elapsed: ", response.elapsed)
print("Request: ", response.request)
print("Content: ", response._content)

# 27. Write a Python program to verifiy SSL certificates for HTTPS requests using requests module. 
# Note: Requests verifies SSL certificates for HTTPS requests, just like a web browser. By default, SSL verification is enabled, and Requests will throw a SSLError if it's unable to verify the certificate
import requests
print(requests.get('https://w3resource.com'))
print(requests.get('https://wayback.com'))
  
