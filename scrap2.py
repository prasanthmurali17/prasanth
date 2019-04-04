#! /usr/bin/env python
import bs4
from urllib2 import Request, urlopen, URLError, HTTPError
from bs4 import BeautifulSoup as soup


my_url="http://snsct.org/?q=faculty-list/19"
uClient=urlopen(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

print "Content-type: text/html\n\n"
print "<html><head><link rel='stylesheet' type='text/css' href='index.css'></head>\n<body>"
print "<div style=\"width:100%;\"><table class='table table-striped' id='staff' style=''><tr scope='col' style='width:auto;color:red;font-size:30px;'><td>"
for record in page_soup.findAll('tr'):
	print record
print "</td></tr></table>   </div>\n</body>\n</html>"


