# 1. Write a Python program to find the title tags from a given html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Title of the document:")
print(soup.find("title"))


# 2. Write a Python program to retrieve all the paragraph tags from a given html document. 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("All paragraph tags:")
print(soup.find_all("p"))

# 3. Write a Python program to get the number of paragraph tags of a given html document. 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Number of paragraph tags:")
print(len(soup.find_all("p")))

# 4. Write a Python program to extract the text in the first paragraph tag of a given html document. 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("The text in the first paragraph tag:")
print(soup.find_all('p')[0].text)

# 5. Write a Python program to find the length of the text of the first < h2 > tag of a given html document. 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Length of the text of the first <h2> tag:")
print(len(soup.find('h2').text))

# 6. Write a Python program to find the text of the first < a > tag of a given html text. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Text of the first <a> tag:")
print(soup.find('a').text)

# 7. Write a Python program to find the href of the first < a > tag of a given html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("href of the first <a> tag:")
print(soup.find('a').attrs['href'])

# 8. Write a Python program to extract all the URLs from the webpage python.org that are nested within < li > tags from . 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

urls = []
for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])
print(urls)

# 9. Write a Python program to find all the h2 tags and list the first four from the webpage python.org. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("First four h2 tags from the webpage python.org.:")
print(soup.find_all('h2')[0:4])

# 10. Write a Python program to find all the link tags and list the first ten from the webpage python.org. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("First four h2 tags from the webpage python.org.:")
print(soup.find_all('a')[0:10])

# 11. Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("List of all the h1, h2, h3 :")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.name + ' ' + heading.text.strip())

# 12. Write a Python program to extract all the text from a given web page. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("Text from the said page:")
print(soup.get_text())

# 13. Write a Python program to print the names of all HTML tags of a given web page going through the document tree. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nNames of all HTML tags (https://www.python.org):\n")
for child in soup.recursiveChildGenerator():
    if child.name:
        print(child.name)

# 14. Write a Python program to retrieve children of the html tag from a given web page. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nChildren of the html tag (https://www.python.org):\n")
root = soup.html    
root_childs = [e.name for e in root.children if e.name is not None]
print(root_childs)

# 15. Write a Python program to retrieve all descendants of the body tag from a given web page. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nDescendants of the body tag (https://www.python.org):\n")
root = soup.html    
root_childs = [e.name for e in root.descendants if e.name is not None]
print(root_childs)

# 16. Write a Python program to retrieve the HTML code of the title, its text, and the HTML code of its parent. 
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("title")
print(soup.title)
print("title text")
print(soup.title.text)
print("Parent content of the title:")
print(soup.title.parent)

# 17. Write a Python program to find and print all li tags of a given web page. 
url = 'https://www.w3resource.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nFind and print all li tags:\n")
for tag in soup.find_all("li"):
    print("{0}: {1}".format(tag.name, tag.text))

# 18. Write a Python program to print content of elements that contain a specified string of a given web page. 
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nContent of elements that contain 'Python' string:")
str1 = soup.find_all(string=re.compile('Python'))
for txt in str1:
    print(" ".join(txt.split()))

# 19. Write a Python program to print the element(s) that has a specified id of a given web page. 
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nelement(s) that has #python-network id:\n")
print(soup.select_one("#python-network"))

# 20. Write a Python program to create a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each HTML/XML tag and string. 
from bs4 import BeautifulSoup
str1 = "<p>Some<b>bad<i>HTML Code</i></b></p>"
print("Original string:")
print(str1)
soup = BeautifulSoup("<p>Some<b>bad<i>HTML Code</i></b></p>", "xml")
print("\nFormatted Unicode string:")
print(soup.prettify())

# 21. Write a Python program to find the first tag with a given attribute value in an html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "lxml")
print(soup.find( href="https://www.w3resource.com/css/CSS-tutorials.php"))

# 22. Write a Python program to find tag(s) beneath other tag(s) in a given html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,"lxml")
print("\na tag(s) Beneath body tag:")
print(soup.select("body a"))
print("\nBeneath html head:")
print(soup.select("html head title"))

# 23. Write a Python program to find tag(s) directly beneath other tag(s) in a given html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,"lxml")
print("\nBeneath directly head tag:")
print(soup.select("head > title"))
print()
print("\nBeneath directly p tag:")
print(soup.select("p > a")) 

# 24. Write a Python program to find the siblings of tags in a given html document. 
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
<a class="sister" href="http://example.com/lacie" id="link1">Lacie</a>
<a class="sister" href="http://example.com/tillie"  id="link2">Tillie</a>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "lxml")
print("\nSiblings of tags:")
print(soup.select("#link1 ~ .sister"))
print(soup.select("#link1 + .sister"))

# 25. Write a Python program to find tags by CSS class in a given html document. 
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a class="sister" href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
<a class="sister" href="http://example.com/lacie" id="link1">Lacie</a>
<a class="sister" href="http://example.com/tillie"  id="link2">Tillie</a>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,"lxml")
print("\nTags by CSS class:")
print(soup.select(".sister"))

# 26. Write a Python program to change the tag's contents and replace with the given string. 
from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>example.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
tag = soup.a
print("\nOriginal Markup:")
print(tag)
print("\nOriginal Markup with new text:")
tag.string = "CSS"
print(tag)

# 27. Write a Python program to add to a tag's contents in a given html document. 
from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>w3resource.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
print("\nOriginal Markup:")
print(soup.a)
soup.a.append("CSS")
print("\nAfter append a text in the new link:")
print(soup.a)

# 28. Write a Python program to insert a new text within a url in a specified position. 
from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>w3resource.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
tag = soup.a
print("Original Markup:")
print(tag.contents)
tag.insert(2, "CSS") #2-> Position of the text (1, 2, 3…)
print("\nNew url after inserting the text:")
print(tag.contents)

# 29. Write a Python program to insert tags or strings immediately before specified tags or strings. 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>", "lxml")
print("Original Markup:")
print(soup.b)
tag = soup.new_tag("i")
tag.string = "Python"
print("\nNew Markup, before inserting the text:")
soup.b.string.insert_before(tag)
print(soup.b)

# 30. Write a Python program to insert tags or strings immediately after specified tags or strings. 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>", "lxml")
print("Original Markup:")
print(soup.b)
tag = soup.new_tag("i")
tag.string = "Python"
print("\nNew Markup, after inserting the text:")
soup.b.string.insert_after(tag)
print(soup.b)

# 31. Write a Python program to remove the contents of a tag in a given html document. 
from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
print(soup.a)
tag = soup.a
tag = tag.clear()
print("\nAfter clearing the contents in the tag:")
print(soup.a)

# 32. Write a Python program to extract a tag or string from a given tree of html document. 
from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
print(soup.a)
i_tag = soup.i.extract()
print("\nExtract i tag from said html Markup:")
print(i_tag)

# 33. Write a Python program to remove a tag from a given tree of html document and destroy it and its contents. 
from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
a_tag = soup.a
print(a_tag)
new_tag = soup.a.decompose()
print("After decomposing:")
print(new_tag)

# 34. Write a Python program to remove a tag or string from a given tree of html document and replace it with the given tag or string. 
from bs4 import BeautifulSoup
html_markup= '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_markup, "lxml")
print("Original markup:")
a_tag = soup.a
print(a_tag)
new_tag = soup.new_tag("b")
new_tag.string = "PHP"
b_tag = a_tag.i.replace_with(new_tag)
print("New Markup:")
print(a_tag)

# 35. Write a Python program to wrap an element in the specified tag and create the new wrapper. 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Python exercises.</p>", "lxml")
print("Original Markup:")
print(soup.p.string.wrap(soup.new_tag("i")))
print("\nNew Markup:")
print(soup.p.wrap(soup.new_tag("div")))

# 36. Write a Python program to replace a given tag with whatever's inside a given tag. 
from bs4 import BeautifulSoup
markup = '<a href="https://w3resource.com/">Python exercises.<i>w3resource.com</i></a>'
soup = BeautifulSoup(markup, "lxml")
a_tag = soup.a
print("Original markup:")
print(a_tag)
a_tag.i.unwrap()
print("\nAfter unwrapping:")
print(a_tag)

