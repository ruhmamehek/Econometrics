import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
# import pandas as pd
  
archive_url ="https://iiitd.ac.in/academics/resources" 
archive_url="https://www.datanetindia-ebooks.com/District_Factbook"

  
def get_links(): 
      
    # create response object 
    r = requests.get(archive_url) 
      
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'html5lib') 
      
    # find all links on web-page 
    links = soup.findAll('a') 

    # filter the link sending with .pdf 
    # _links = [archive_url + link['href'] for link in links if link['href'].contains('.pdf')] 
    # i=0
    _links=[]
    # print(links)
    for link in links:
        try:
    # if link['href'].endswith('.pdf'):
            if ("Chandigarh") in link["href"]:
                _links.append("https://www.datanetindia-ebooks.com"+link["href"])
            # print(archive_url+link["href"])
        except:
            print("rejected ", link)
            # continue

    print(_links)
    return _links 
  
  
def download_series(_links): 
  
    for link in _links: 
  
        '''iterate through all links in _links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string 
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name) 
          
        # create response object 
        r = requests.get(link, stream = True) 
          
        # download started 
        with open(file_name, 'wb') as pdf: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    pdf.write(chunk) 
          
        print("%s downloaded!\n"%file_name) 
  
    print("All files downloaded!")
    return
  
  

  
 
_links = get_links()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path="C:/Users/ruhma/Downloads/chromedriver_win32")
for link in _links:

	URL=link
	driver.maximize_window()
	driver.get(URL)
	time.sleep(5)
	# content=requests.get(URL)
	# soup = BeautifulSoup(content.text, 'html.parser')
	# soup.find('div', id = "divDHBT")
	# print(soup)
	# print(soup.findAll("div", {"id": "divDHBT"}))
	# print (soup.find('div', id = "divDHBT"))
	# print(len(soup))
	content = driver.page_source.encode('utf-8').strip()
	soup = BeautifulSoup(content,"html.parser")
	officials = soup.findAll("div",{"id":"divDHBT"})
	
	for entry in officials:
	    print(str(entry))










# url= "http://www.pro-football-reference.com/boxscores/201309050den.htm"






driver.quit()

# download_series(_links)
