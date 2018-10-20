# couldn't use BeautifulSoup library because webpage is rendered dynamically with javascript
from selenium import webdriver

webDriver = webdriver.Chrome('/Users/trevorfox/PycharmProjects/zumeScraper/chromedriver')
webDriver.get('https://www.buildingconnected.com/jobs/')

for count, i in enumerate(webDriver.find_elements_by_class_name("css-12xrnu5")):
    print(str(count+1) + '. ' + i.text.replace('\n',' ').replace('VIEW', ''))

webDriver.close()
