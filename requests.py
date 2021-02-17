# Requests is an elegant and simple HTTP library for Python, built for human beings. Requests allows you to send HTTP/1.1 requests extremely easily. There's no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100 % automatic.

# 1. Write a Python code to find the Requests module - version, licence, copyright information, author, author email, document url, title and description. 
import requests
print("Python Requests module - version:", requests.__version__)
print("Licence:", requests. __license__)
print("Copyright:", requests.__copyright__)
print("Author:", requests.__author__)
print("Author email:", requests.__author_email__)
print("Document url, title, description:")
print(requests.__url__)
print(requests.__title__)
print(requests.__description__)

# 2. Write a Python code to check the status code issued by a server in response to a client's request made to the server. Print all of the methods and attributes available to objects on successful request. 
res = requests.get('https://google.com/')
print("Response of https://google.com/:")
print(res.status_code)
res = requests.get('https://amazon.com/')
print("Response of https://amazon.com/:")
print(res.status_code)
res = requests.get('https://w3resource.com/')
print("Response of https://w3resource.com/:")
print(res.status_code)
print("\nMethods and attributes available to objects on successful\nrequest of https://w3resource.com:\n")
print(dir(res))

# 3. Write a Python code to send a request to a web page, and print the response text and content. Also get the raw socket response from the server. 
res = requests.get('https://www.google.com/')
print("Response text of https://google.com/:")
print(res.text)
print("\n==============================================================================")
print("\nContent of the said url:")
print(res.content)
print("\n==============================================================================")
print("\nRaw data of the said url:")
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
print(r.raw.read(15))

# 4. Write a Python code to send a request to a web page, and print the information of headers. Also parse these values and print key-value pairs holding various information. 
r = requests.get('https://api.github.com/')
response = r.headers
print("Headers information of the said response:")
print(response)
print("\nVarious Key-value pairs information of the said resource and request:")

print("Date: ", r.headers['date'])
print("server: ", r.headers['server'])
print("status: ", r.headers['status'])
print("cache-control: ", r.headers['cache-control'])
print("vary: ", r.headers['vary'])
print("x-github-media-type: ", r.headers['x-github-media-type'])
print("access-control-expose-headers: ",
      r.headers['access-control-expose-headers'])
print("strict-transport-security: ", r.headers['strict-transport-security'])
print("x-content-type-options: ", r.headers['x-content-type-options'])
print("x-xss-protection: ", r.headers['x-xss-protection'])
print("referrer-policy: ", r.headers['referrer-policy'])
print("content-security-policy: ", r.headers['content-security-policy'])
print("content-encoding: ", r.headers['content-encoding'])
print("X-Ratelimit-Remaining: ", r.headers['X-Ratelimit-Remaining'])
print("X-Ratelimit-Reset: ", r.headers['X-Ratelimit-Reset'])
print("X-Ratelimit-Used: ", r.headers['X-Ratelimit-Used'])
print("Accept-Ranges:", r.headers['Accept-Ranges'])
print("X-GitHub-Request-Id:", r.headers['X-GitHub-Request-Id'])

# 5. Write a Python code to send a request to a web page, and print the JSON value of the response. Also print each key value of the response. 
r = requests.get('https://api.github.com/')
response = r.json()
print("JSON value of the said response:")
print(r.json())
print("\nEach key of the response:")
print("Current user url:", response['current_user_url'])
print("Current user authorizations html url:",
      response['current_user_authorizations_html_url'])
print("Authorizations url:", response['authorizations_url'])
print("code_search_url:", response['code_search_url'])
print("commit_search_url:", response['commit_search_url'])
print("Emails url:", response['emails_url'])
print("Emojis url:", response['emojis_url'])
print("Events url:", response['events_url'])
print("Feeds url:", response['feeds_url'])
print("Followers url:", response['followers_url'])
print("Following url:", response['following_url'])
print("Gists url:", response['gists_url'])
print("Issue search url:", response['issue_search_url'])
print("Issues url:", response['issues_url'])
print("Keys url:", response['keys_url'])
print("label search url:", response['label_search_url'])
print("Notifications url:", response['notifications_url'])
print("Organization url:", response['organization_url'])
print("Organization repositories url:",
      response['organization_repositories_url'])
print("Organization teams url:", response['organization_teams_url'])
print("Public gists url:", response['public_gists_url'])
print("Rate limit url:", response['rate_limit_url'])
print("Repository url:", response['repository_url'])
print("Repository search url:", response['repository_search_url'])
print("Current user repositories url:",
      response['current_user_repositories_url'])
print("Starred url:", response['starred_url'])
print("Starred gists url:", response['starred_gists_url'])
print("User url:", response['user_url'])
print("User organizations url:", response['user_organizations_url'])
print("User repositories url:", response['user_repositories_url'])
print("User search url:", response['user_search_url'])

# 6. Write a Python code to send a request to a web page and stop waiting for a response after a given number of seconds. In the event of times out of request, raise Timeout exception. 
print("timeout = 0.001")
try:
    r = requests.get('https://github.com/', timeout=0.001)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)

print("\ntimeout = 1.0")
try:
    r = requests.get('https://github.com/', timeout=1.0)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)

# 7. Write a Python code to send some sort of data in the URL's query string. 
payload = {'key1': 'value1', 'key2': 'value2'}
print("Parameters: ", payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)
print("\nPass a list of items as a value:")
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
print("Parameters: ", payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)

# 8. Write a Python code to send cookies to a given server and access cookies from the response of a server. 
url = 'http://httpbin.org/cookies'
# A dictionary (my_cookies) of cookies to send to the specified url.
my_cookies = dict(
    cookies_are='Cookies parameter use to send cookies to the server')
r = requests.get(url, cookies=my_cookies)
print(r.text)
# Accessing cookies with Requests
# url = 'http://WebsiteName/cookie/setting/url'
# res = requests.get(url)
# Value of cookies
# print(res.cookies['cookie_name'])

# 9. Write a Python code to verify the SSL certificate for a website which is certified. 
#Requests ignore verifying the SSL certificate if you set verify to False
# Making a get request
response = requests.get('https://rigaux.org/', verify=False)
print(response)
print("\n=======================================================\n")
#Requests verifies SSL certificates for HTTPS requests, just like a web browser.
response1 = requests.get('https://google.com/')
print(response1)
print("\n=======================================================\n")
#Requests ignore verifying the SSL certificate if you set verify to True (Default value)
response1 = requests.get('https://rigaux.org/', verify=True)
print(response1)
